import numpy as np
import scipy.optimize
from scipy.optimize import fsolve
from functools import partial
from itertools import repeat
import requests
import pandas as pd
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from statsmodels.tsa.holtwinters import SimpleExpSmoothing, Holt
import csv
from datetime import datetime

#define array for a,b,c
out_array=[];r=1;k=0;period=4;sm=1;u=0;data=[];small_data=[];g=0;start=0;end=0;temp_data=[];temp_data_y=[];deduct=0;start_old=0;finished=False;A_value1=[];B_value1=[]
A_value2=[];B_value2=[];A_value3=[];B_value3=[];A_value4=[];B_value4=[];A_value5=[];B_value5=[]
main=[];country="";start=0;end=0;dat="";dates=0;date_diff_array=[];diff=0;arry_num=[];u=0;f=0;infected_array=[];country_f="";i=0;a=0;b=0;counter=0
p=0;tem_main=[];old_m=0;rep=0;t_out=0;city="";rounding=0;
     
#create the production array


######################################################## READ FROM CSV FILE ########################################################################

print("	1	1/22/2020	11	2/1/2020	21	2/11/2020	31	2/21/2020	41	3/2/2020	")
print("	2	1/23/2020	12	2/2/2020	22	2/12/2020	32	2/22/2020	42	3/3/2020	")
print("	3	1/24/2020	13	2/3/2020	23	2/13/2020	33	2/23/2020	43	3/4/2020	")
print("	4	1/25/2020	14	2/4/2020	24	2/14/2020	34	2/24/2020	44	3/5/2020	")
print("	5	1/26/2020	15	2/5/2020	25	2/15/2020	35	2/25/2020	45	3/6/2020	")
print("	6	1/27/2020	16	2/6/2020	26	2/16/2020	36	2/26/2020	46	3/7/2020	")
print("	7	1/28/2020	17	2/7/2020	27	2/17/2020	37	2/27/2020	47	3/8/2020	")
print("	8	1/29/2020	18	2/8/2020	28	2/18/2020	38	2/28/2020	48	3/9/2020	")
print("	9	1/30/2020	19	2/9/2020	29	2/19/2020	39	2/29/2020	49	3/10/2020	")
print("	10	1/31/2020	20	2/10/2020	30	2/20/2020	40	3/1/2020	50	3/11/2020	")
print("											")
print("	51	3/12/2020	61	3/22/2020	71	4/1/2020	81	4/11/2020	91	4/21/2020	")
print("	52	3/13/2020	62	3/23/2020	72	4/2/2020	82	4/12/2020	92	4/22/2020	")
print("	53	3/14/2020	63	3/24/2020	73	4/3/2020	83	4/13/2020	93	4/23/2020	")
print("	54	3/15/2020	64	3/25/2020	74	4/4/2020	84	4/14/2020	94	4/24/2020	")
print("	55	3/16/2020	65	3/26/2020	75	4/5/2020	85	4/15/2020	95	4/25/2020	")
print("	56	3/17/2020	66	3/27/2020	76	4/6/2020	86	4/16/2020	96	4/26/2020	")
print("	57	3/18/2020	67	3/28/2020	77	4/7/2020	87	4/17/2020			")
print("	58	3/19/2020	68	3/29/2020	78	4/8/2020	88	4/18/2020			")
print("	59	3/20/2020	69	3/30/2020	79	4/9/2020	89	4/19/2020			")
print("	60	3/21/2020	70	3/31/2020	80	4/10/2020	90	4/20/2020			")

print("Please enter up to 5 countries as shown in the examples")
print("example 1: enter 3 countries as (Austria,Bahrain,Chile)")
print("example 2; enter two countries with cities(Australia:New SOuth Wales,China:Fujian)")
entry_c=input("? ")
country_array=entry_c.split(",")
#start_date=input("Enter the start date ?[1-79] ")
start_date=1
#end_date=input("Enter the end date ?[1-79] ")
end_date=81

def in_to_num(argument):
	switcher={
			1: "43852",2: "43853",3: "43854",4: "43855",5: "43856",6: "43857",7: "43858",8: "43859",9: "43860",10: "43861",
			11: "43862",12: "43863",13: "43864",14: "43865",15: "43866",16: "43867",17: "43868",18: "43869",19: "43870",20: "43871",
			21: "43872",22: "43873",23: "43874",24: "43875",25: "43876",26: "43877",27: "43878",28: "43879",29: "43880",30: "43881",
			31: "43882",32: "43883",33: "43884",34: "43885",35: "43886",36: "43887",37: "43888",38: "43889",39: "43890",40: "43891",
			41: "43892",42: "43893",43: "43894",44: "43895",45: "43896",46: "43897",47: "43898",48: "43899",49: "43900",50: "43901",
			51: "43902",52: "43903",53: "43904",54: "43905",55: "43906",56: "43907",57: "43908",58: "43909",59: "43910",60: "43911",
			61: "43912",62: "43913",63: "43914",64: "43915",65: "43916",66: "43917",67: "43918",68: "43919",69: "43920",70: "43921",
			71: "43922",72: "43923",73: "43924",74: "43925",75: "43926",76: "43927",77: "43928",78: "43929",79: "43930",80: "43931",
                        81: "43932",82: "43933",83: "43934",84: "43935",85: "43936",86: "43937",87: "43938",88: "43939",89: "43940",90: "43941"
			
		 }
	return switcher.get(argument, "nothing")
			 
#create an array for the period chosen
start=int(start_date)
end=int(end_date)
date_diff_array=list(range(start,end+1))
for diff in date_diff_array:
	dat_num=in_to_num(diff)
	arry_num.insert(u,dat_num)
	u+=1
#dat_num=in_to_num()
for cntry in country_array:
        if ":" in cntry:
                cnt=cntry.split(":")
                country=cnt[0]
                city=cnt[1]
        else:
                country=cntry
        with open('time_series_covid19_confirmed_global2.csv', newline='') as csvfile:
                spam=csv.DictReader(csvfile)
                for row in spam:
                         country_f=row['Country/Region']
                         city_f=row['Province/State']
                         if city=="":
                                 
                                 if country_f==country:
                                         
                                         for vv in arry_num:
                                                 infected_array.append(row[str(vv)])
                         if city!="":
                                 if country_f==country and city_f==city:
                                         for vv in arry_num:
                                                 infected_array.append(row[str(vv)])
                          

        
        main=[]
        ####################################################### END OF CSV FILE READING ########################################################################																								 

        #convert the string of the list to int
        for i in infected_array: 
            main.append(int(i))
        #end=(len(main)//period)
        infected_array=[]

        print("repeated",main)
        def jump(rep,t):
            if rep>=1:
                    t_out0=t*0.5+t
                    t_out=t_out0
            if rep>=2:
                    t_out1=t_out0*0.5+t_out0
                    t_out=t_out1
            if rep>=3:
                    t_out2=t_out1*0.5+t_out1
                    t_out=t_out2
            if rep>=4:
                    t_out3=t_out2*0.5+t_out2
                    t_out=t_out3
            if rep>=5:
                    t_out4=t_out3*0.5+t_out3
                    t_out=t_out4
            if rep>=6:
                    t_out5=t_out4*0.5+t_out4
                    t_out=t_out5
            if rep>=7:
                    t_out6=t_out5*0.5+t_out5
                    t_out=t_out6
            if rep>=8:
                    t_out7=t_out6*0.5+t_out6
                    t_out=t_out7
            if rep>=9:
                    t_out8=t_out7*0.5+t_out7
                    t_out=t_out8
            if rep>=10:
                    t_out9=t_out8*0.5+t_out8
                    t_out=t_out9
            else:
                    t_out=1
                    
            return t_out

        #remove the repeated data, check if the data has jump. The jump definition
        
        for m in main:
            if p==0:
                    old_m=m
                    tem_main.append(m)
            if p>0:
                    if old_m==m:
                            rep+=1
                            old_m=m
                    if old_m!=m and rep==0:
                            tem_main.append(m)
                            old_m=m
                    if old_m!=m and rep>0:
                            jump_rs=jump(rep,old_m)
                            rep=0
                            tem_main.append(m)
                            old_m=m
                #if jump_rs
                    
            p+=1
            
        main=tem_main
        tem_main=[]
        
        print("the main ",main)  

        i=0;e=0
        def G(small_data, x):
                return np.cos(x) +x[::1] - small_data
                


        end=period
        start=0
        start_old=0
        stop=False
        k=0

        #decide the next small array
        
        for m in main:
            if stop==False:
                    if k<len(main)-3:
                            k+=period
                            small_data=main[start:end]
                            start=end
                            end+=period
                   
                    if start==start_old:
                            stop=True
                    
                
                    
                    G_partial = partial(G, small_data)
                    approximate=list(repeat(1,period))
                    
                    y = scipy.optimize.broyden1(G_partial, approximate, f_tol=90000000000000e-14)
                    
                    
                    
                    
                    start_old=start
                    
                    
                    #find a and b
                    b=(y[r+2]/y[r])**(1/(small_data[r+2]-small_data[r]))
                    a=y[r]/(b**small_data[r])
                    if rounding==0:
                            A_value1.append(a)
                            B_value1.append(b)
                            a=0;b=0
                            
                
                    if rounding==1:
                            A_value2.append(a)
                            B_value2.append(b)
                            a=0;b=0
                            
                    if rounding==2:
                            A_value3.append(a)
                            B_value3.append(b)
                            a=0;b=0
                            
                    if rounding==3:
                            A_value4.append(a)
                            B_value4.append(b)
                            a=0;b=0
                            
                    if rounding==4:
                            A_value5.append(a)
                            B_value5.append(b)
                            a=0;b=0
                            
        
        counter+=1
        rounding+=1
        #main=[]
if A_value1!=[]:
        A_value1.pop()
        B_value1.pop()
        print("the A for ",country_array[0]," :",A_value1)
        print("the B for ",country_array[0]," :",B_value1)
if A_value2!=[]:
        A_value2.pop()
        B_value2.pop()
        print("the A for ",country_array[1]," :",A_value2)
        print("the B for ",country_array[1]," :",B_value2)
if A_value3!=[]:
        A_value3.pop()
        B_value3.pop()
        print("the A for ",country_array[2]," :",A_value3)
        print("the B for ",country_array[2]," :",B_value3)
if A_value4!=[]:
        A_value4.pop()
        B_value4.pop()
        print("the A for ",country_array[3]," :",A_value4)
        print("the B for ",country_array[3]," :",B_value4)
if A_value5!=[]:
        A_value5.pop()
        B_value5.pop()
        print("the A for ",country_array[4]," :",A_value5)
        print("the B for ",country_array[4]," :",B_value5)
              
#####################   GRAPH THE RESULTS
# Function to plot

lists=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
if A_value1!=[]:
        counter=len(A_value1)
        x1=lists[0:counter]
        Val1="A value for "+country_array[0]
        Val2="B value for "+country_array[0]
        plt.plot(x1,A_value1,"-b",label=Val1) 
        plt.plot(x1,B_value1,"-r",label=Val2)
        plt.legend(loc="upper left")
   
        
if A_value2!=[]:
        
        counter=len(A_value2)
        x1=lists[0:counter]
        Val1="A value for "+country_array[1]
        Val2="B value for "+country_array[1]
        plt.plot(x1,A_value2,"-g",label=Val1) 
        plt.plot(x1,B_value2,"-y",label=Val2)        
        plt.legend(loc="upper left")
        
if A_value3!=[]:
        counter=len(A_value3)
        x1=lists[0:counter]
        Val1="A value for "+country_array[2]
        Val2="B value for "+country_array[2]
        plt.plot(x1,A_value3,"-k",label=Val1) 
        plt.plot(x1,B_value3,"-c",label=Val2)        
        plt.legend(loc="upper left")       

if A_value4!=[]:
        counter=len(A_value4)
        x1=lists[0:counter]
        Val1="A value for "+country_array[3]
        Val2="B value for "+country_array[3]
        plt.plot(x1,A_value4,"#eeefff",label=Val1) 
        plt.plot(x1,B_value4,"#aaefff",label=Val2)        
        plt.legend(loc="upper left")  

if A_value5!=[]:
        counter=len(A_value5)
        x1=lists[0:counter]
        Val1="A value for "+country_array[4]
        Val2="B value for "+country_array[4]
        plt.plot(x1,A_value5,"g",label=Val1) 
        plt.plot(x1,B_value5,"y",label=Val2)        
        plt.legend(loc="upper left")  

plt.show()





