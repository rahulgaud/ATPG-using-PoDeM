''' Submitted by 
            Aashish Pandia 203196001
            Prasad Trimukhe 203076001
            Rahul Gaud 203070029
            
to run this code "./python PODeM_final.py"
'''

# txt1 = ['AND 2 IN 1 2 OP 4', 'NOT 1 IN 3 OP 5', 'OR 2 IN 4 5 OP 6', 'AND 2 IN 1 6 OP 7' ] #'OR 2 IN 4 7 OP 8', 'AND 2 IN 5 8 OP 10']
from operator import itemgetter
txt1 = []
f = open("podem_netlist.txt", "r")
for x in f:
  txt1.append(x)
f.close()


def AND_logic(List):
    # print(List)
    inp1 = List[0]
    inp2 = List[1]
    
    if inp1 == [0,'A']:
        out_gate = [0,'A']
        return out_gate

    if inp2 == [0,'A']:
        out_gate = [0,'A']
        return out_gate
    
    if inp1 == [0,'F']:
        out_gate = [0,'F']
        return out_gate
    
    if inp2 == [0,'F']:
        out_gate = [0,'F']
        return out_gate

    if inp1 == [1,'A']:
        out_gate = inp2
        return out_gate
    
    if inp2 == [1,'A']:
        out_gate = inp1
        return out_gate

    if inp1[1] == "x" :
        out_gate = inp1
        return out_gate
    
    if inp2[1] == "x" :
        out_gate = inp2
        return out_gate
        
    if inp1 == [1,'F'] and inp2 == [1,'F']:
        out_gate = [1,'F']
        return out_gate

def OR_logic(List):
    # print(List)
    inp1 = List[0]
    inp2 = List[1]
    
    if inp1 == [1,'A']:
        out_gate = [1,'A']
        return out_gate

    if inp2 == [1,'A']:
        out_gate = [1,'A']
        return out_gate
    
    if inp1 == [1,'F']:
        out_gate = [1,'F']
        return out_gate
    
    if inp2 == [1,'F']:
        out_gate = [1,'F']
        return out_gate

    if inp1 == [0,'A']:
        out_gate = inp2
        return out_gate
    
    if inp2 == [0,'A']:
        out_gate = inp1
        return out_gate

    if inp1[1] == "x" :
        out_gate = inp1
        return out_gate
    
    if inp2[1] == "x" :
        out_gate = inp2
        return out_gate
        
    if inp1 == [0,'F'] and inp2 == [0,'F']:
        out_gate = [0,'F']
        return out_gate

def NAND_logic(List):
    # print(List)
    inp1 = List[0]
    inp2 = List[1]
    
    if inp1 == [0,'A']:
        out_gate = [1,'A']
        return out_gate

    if inp2 == [0,'A']:
        out_gate = [1,'A']
        return out_gate
    
    if inp1 == [0,'F']:
        out_gate = [1,'F']
        return out_gate
    
    if inp2 == [0,'F']:
        out_gate = [1,'F']
        return out_gate

    if inp1 == [1,'A']:
        out_gate = [ int(not inp2[0]),inp2[1] ]
        return out_gate
    
    if inp2 == [1,'A']:
        out_gate = [ int(not inp1[0]),inp2[1] ]
        return out_gate

    if inp1[1] == "x" :
        out_gate = inp1
        return out_gate
    
    if inp2[1] == "x" :
        out_gate = inp2
        return out_gate
        
    if inp1 == [1,'F'] and inp2 == [1,'F']:
        out_gate = [0,'F']
        return out_gate

def NOR_logic(List):
    # print(List)
    inp1 = List[0]
    inp2 = List[1]
    
    if inp1 == [1,'A']:
        out_gate = [0,'A']
        return out_gate

    if inp2 == [1,'A']:
        out_gate = [0,'A']
        return out_gate
    
    if inp1 == [1,'F']:
        out_gate = [0,'F']
        return out_gate
    
    if inp2 == [1,'F']:
        out_gate = [0,'F']
        return out_gate

    if inp1 == [0,'A']:
        out_gate = [ int(not inp2[0]),inp2[1] ]
        return out_gate
    
    if inp2 == [0,'A']:
        out_gate = [ int(not inp1[0]),inp2[1] ]
        return out_gate

    if inp1[1] == "x" :
        out_gate = inp1
        return out_gate
    
    if inp2[1] == "x" :
        out_gate = inp2
        return out_gate
        
    if inp1 == [0,'F'] and inp2 == [0,'F']:
        out_gate = [1,'F']
        return out_gate

def NOT_logic(List):
    # print(List)
    if List[0][1] == 'x':
        out_gate = [0,'x']
        return out_gate
        
    else:
        out_gate = [int(not List[0][0]),List[0][1]]
        return out_gate
    
def function_decoder(String):
    global net_values
    String_list = String.split()
    func = String_list[0]
    func_inps = []
    func_outs = 0
    for index,word in enumerate(String_list):
        if word == 'IN':
            no_of_ins = int(String_list[index-1])
            # print(int(String_list[index-1]))
            for inp in range(no_of_ins):
                func_inps.append(int(String_list[index+1 + inp]))
        if word == 'OP':
           func_outs = int(String_list[index+1])
            
    # print(func_inps,"->",func_outs) 
    operation = [ func, func_inps, func_outs, -20, False]
    return operation

list_of_input_edges = []
list_of_OP_edges = []

netlist_to_sim = []

Global_stack = []


for line in txt1:
    var1 = function_decoder(line)
    netlist_to_sim.append(var1)

    for edge in var1[1]:
        if edge not in list_of_OP_edges:
            if edge not in list_of_input_edges:
                list_of_input_edges.append(edge)
    var2 = var1[2]
    if var2 not in list_of_OP_edges:
        list_of_OP_edges.append(var2)


finished_edges = list_of_input_edges.copy()

total_edges = list_of_input_edges + list_of_OP_edges

list_of_input_edges.sort()
total_edges.sort()
list_of_OP_edges.sort()

list_of_OUTPUT_edges = []     # different from list_of_OP_edges; final output nodes only
for i in list_of_OP_edges:
    flag_var = True
    for j in range(len(netlist_to_sim)):
        if i in netlist_to_sim[j][1]:
            # if i not in list_of_OUTPUT_edges:
                flag_var = False
    if flag_var: 
        list_of_OUTPUT_edges.append(i)
        flag_var = False

net_values = { _ : [0,"x"] for _ in total_edges} #[0] * len(total_nodes)

level = 1
for itterr in range(len(netlist_to_sim)):
    index_var = []
    # print(finished_edges, "\n")
    for index, gate_test in enumerate(netlist_to_sim):
        flag_var1 = False
        flag_var2 = False
        # print("entry --->",gate_test)
        if gate_test[0] == 'NOT':
            in1 = gate_test[1][0]
            if in1 in finished_edges :
                index_var.append(index)
                if not gate_test[-1]:
                    netlist_to_sim[index][3] = level
                    gate_test[-1] = True
        
        else:
            in1 = gate_test[1][0]
            in2 = gate_test[1][1]
            if in1 in finished_edges :
                # print(in1 ,"-1 found in",finished_edges )
                flag_var1 = True
            if in2 in finished_edges :
                flag_var2 = True
                # print(in2 ,"-2 found in",finished_edges )
    
            if flag_var1 and flag_var2:
                index_var.append(index)
                if not gate_test[-1]:
                    netlist_to_sim[index][3] = level
                    gate_test[-1] = True
                
    for k in index_var:
        if netlist_to_sim[k][2] not in finished_edges:
            finished_edges.append(netlist_to_sim[k][2])  
    level+=1
for gate_des in netlist_to_sim:
    gate_des[-1] = False

levelized_netlist = sorted(netlist_to_sim, key=itemgetter(3))    

def gate_sim(List):   #list generated by fn_deco 
    # print(List)
    gate_already_done = List[-1]
    if gate_already_done:
       return 
    for edge in List[1]:
        operands = [ net_values[_] for _ in List[1]]
        # print(operands)
        if List[0] == 'AND':
            net_values[List[2]]  = AND_logic(operands) 
            
        if List[0] == 'NAND':
            net_values[List[2]]  = NAND_logic(operands)
            
        if List[0] == 'OR':
            net_values[List[2]]  = OR_logic(operands) 
        
        if List[0] == 'NOR':
            net_values[List[2]]  = NOR_logic(operands) 
                
        if List[0] == 'NOT':
            net_values[List[2]]  = NOT_logic(operands) 
        
        List[-1] = True 
        # finished_edges.append(List[-2])
            
def forward_simulation(given_netlist):
    global net_values
    for gate_test in given_netlist:
        gate_sim(gate_test)
        
    # for i in list_of_OUTPUT_edges :
    #     print("net no", i , "net output", net_values[i], end='\n')
    
    # reset gate done status for next simulaation
    for gate_des in given_netlist:
        gate_des[-1] = False

def sim_reset(given_netlist):
    for gate_des in given_netlist:
        gate_des[-1] = False


#%% 
input_vec = [1,2,3]
input_vals = [[1,'A'],[0,"A"],[1,'A']]
       
print("\n\n---------Start------------\n")
forward_simulation(levelized_netlist)
print("Simulation result" , net_values,"\n\n" )
print("\n\n---------------------\n")
#%%

#-----------------PODeM-----------------------------------------------------


Faulty_egde_location = 4; Fault_type = 1 # 1 = SA1, 0 = SA0;

FD_objective_fn = (Faulty_egde_location, int(not Fault_type))
# print(FD_objective_fn)



net_values = { _ : [0,"x"] for _ in total_edges} #[0] * len(total_nodes)

def Is_Objective_met(objective_tuple):
    # print("YE",net_values[objective_tuple[0]], [int(not objective_tuple[1]),'A'])
    if net_values[objective_tuple[0]] == [objective_tuple[1],'A']:
        return True
    else: return False
    

def complete_objective(objective_tuple):
               
        global net_values
        print('input to obj fn', objective_tuple )
        Objective_value =  objective_tuple[1]
        
        if objective_tuple[0] in list_of_input_edges:
            net_values[objective_tuple[0]][0] = Objective_value
            net_values[objective_tuple[0]][1] = "A"
            print("Setting this primary net ->",objective_tuple[0],"at",net_values[objective_tuple[0]])
            Global_stack.append([objective_tuple[0],net_values[objective_tuple[0]]])
            print("simulating..")
            forward_simulation(levelized_netlist)
            return
            # Is_Objective_met(objective_tuple)
            
            print("Simulation result" , net_values,"\n\n" )
            
        
        else:
            for i in range (len(levelized_netlist)):
                if objective_tuple[0] in levelized_netlist[i]:
                    gate_type = levelized_netlist[i][0] 
                    gate_ins_list = levelized_netlist[i][1]
                    print(gate_type,gate_ins_list)
            # if edge is in primary
            for edge in gate_ins_list:
                if edge in list_of_input_edges:
                    if net_values[edge][1] == "A": # input is already set
                        print("Already set")
                        continue;
                    else:
                        if gate_type[0] == "N":
                            net_values[edge][0] = int(not Objective_value)
                        else: 
                            net_values[edge][0] =  Objective_value

                        net_values[edge][1] = "A"
                        print("Not already set; Setting this net",edge,"at",net_values[edge])
                        Global_stack.append([edge,net_values[edge]])
                        print("simulating.....")
                        forward_simulation(levelized_netlist)
                        print("Simulation result" , net_values,"\n\n" )
                        return
            
            for edge in gate_ins_list:
                if edge not in list_of_input_edges:
                    if net_values[edge][1] == "A": # input is already set
                        print("Already set")
                        continue;
                    else:
                        if gate_type[0] == "N":
                            NoV = int(not Objective_value)
                            NoL = edge
                        else:
                            NoV = Objective_value
                            NoL = edge
                        
                        print("new values incoming -------------")
                        new_obj = (NoL,NoV)
                        complete_objective(new_obj)
                        return


def Fault_sensatization(objective_tuple):
    global net_values
    
    # ab_bas = 0
    print(objective_tuple,"___",net_values[objective_tuple[0]][0], "<--- comparing this ")
    while net_values[objective_tuple[0]][1] == 'x':
        complete_objective(FD_objective_fn)
        # ab_bas+=1
        # if ab_bas > 5:
        #     break
        
    if net_values[objective_tuple[0]][0] != objective_tuple[1] :
        print("\n-----------------> objective can't be reached <---------------\n")

    else: print("fault is sensetized \n")        


Fault_sensatization(FD_objective_fn)
#%%
def Fault_updation(Faulty_egde_no,netlist):
    global net_values

    print("-----Fault updated to net values---------")
    net_values[Faulty_egde_no][1] = 'F'
    for gate_des in netlist:
        if Faulty_egde_no == gate_des[2]:
            gate_des[-1] = True

Fault_updation(Faulty_egde_location,levelized_netlist)

# def Is_Fault_sensetized():
    
for i,j in zip(input_vec,input_vals):
    Global_stack.append([i,j])    
#%%        
def find_Frontier(faulty_loc):
    # print(faulty_loc_and_value_tuple)
    local_list = []   
    for i in range (len(levelized_netlist)):
        if faulty_loc in levelized_netlist[i][1]:
            # if net_values[faulty_loc_and_value_tuple[0]][1] == "x" :
                # frontier_list = netlist_to_sim[i]
                local_list.append(levelized_netlist[i])
    return (local_list)
    
frontier_list = find_Frontier(Faulty_egde_location)

D_front = []
                   
for gate_des in frontier_list:
    if gate_des == 'NOT':
        for i in levelized_netlist:
            if gate_des[2] in levelized_netlist[i][1]:
                D_front.append()
    if net_values[gate_des[2]][1] == "x":
        D_front.append(gate_des)
    

def get_NCV(string):
    if string == "AND":
        return 1
    if string == "OR":
        return 0
    if string == "NAND":
        return 1
    if string == "NOR":
        return 0

    
    
#%%
# if len(D_front) != 0:

new_fault_edge = 0   
def Fault_propagation(Gate_description,Fault_net):
    global new_fault_edge
    if len(Gate_description) != 0:
        in_nets = Gate_description[1] 
        for unassigned_nets in in_nets:
            if unassigned_nets != Fault_net:
                obj_net_no = unassigned_nets
                obj_net_val = get_NCV(Gate_description[0])
        print("propagation objective net = {}, value = {}  ".format(obj_net_no,obj_net_val))
        complete_objective((obj_net_no,obj_net_val))
        sim_reset(levelized_netlist)
        new_fault_edge = Gate_description[2]
    else:
        Global_stack.pop()

Fault_propagation(D_front[0],Faulty_egde_location)
D_front.pop()


for entry in Global_stack:
    net_values[entry[0]] = entry[1]
forward_simulation(levelized_netlist)

Fault_still_present = Is_Objective_met(FD_objective_fn)
# print(Fault_still_present,"Fault_still_present")
if Fault_still_present:
    Fault_updation(Faulty_egde_location,levelized_netlist)
    forward_simulation(levelized_netlist)
    Fault_prop_done = True
    

if Fault_prop_done:
    for i in list_of_input_edges:
        print ("input vector {} = ".format(i), net_values[i])     
else: print ('Fault cant be propagated')



        
        
        
            
































