# Add the functions in this file
import math
import json
correlation_values = { }
def load_journal(name) :
    f = open(name)
    s = f.read()
    global d
    d = json.loads(s)
    return d


def compute_phi(name,event) :
  
    n11 = []
    n00 = []
    n10 = []
    n01 = []
    n1p = []
    n0p = []
    np1 = []
    np0 = []
       
    f = open(name)
    s = f.read()
    d = json.loads(s)
   
    for i in d :
      
        if event in i["events"] and i["squirrel"] == True      : 
           n11.append(1)
        if event not in i["events"] and i["squirrel"] == False :
           n00.append(1)
        if event in i["events"] and i["squirrel"] == False     : 
           n10.append(1)
        if event not in i["events"] and i["squirrel"] == True  :
           n01.append(1)
        if event in i["events"]                               :
           n1p.append(1)
        if event not in i["events"]                           :
           n0p.append(1)
        if i["squirrel"] == True                               :
           np1.append(1)
        if i["squirrel"] == False                              :
           np0.append(1)
         
         
    global correlation
    correlation = ((len(n11)*len(n00))-(len(n10)*len(n01)))/(math.sqrt(len(n1p)*len(n0p)*len(np1)*len(np0)))
    
    
    return(((len(n11)*len(n00))-(len(n10)*len(n01)))/(math.sqrt(len(n1p)*len(n0p)*len(np1)*len(np0))))
     
        



def compute_correlations(name) :   
    
    load_journal(name)
    all_events = set()
    for i in d :
        h =  i["events"]
        for i in h :
           all_events.add(i)
    for i in all_events :        
        compute_phi(name,i)
        correlation_values.update({ i : correlation } )
    return correlation_values   
        
def diagnose(name) :
    compute_correlations(name)
    return(max(correlation_values, key=correlation_values.get)) , (min(correlation_values, key=correlation_values.get))

 
                 
    
    
        



