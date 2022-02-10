import pandas as pd
#file name (or) path of the file
orders=pd.read_csv("10.2.22 Training Datas.csv")        
print("ACTUAL DATASET")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(orders)
print("\n\nTotal no of repeted calls  are: ",orders['NUMBER'].duplicated(). sum())


print("\n\nRepeted no info:")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(orders[orders['NUMBER'].duplicated(keep='last')])

print("\n\n******** The following contacts are may be Spam ********")
l1=list(orders['NAME'].values)
l2=[]
for i in range(0,len(l1)):
    if l1[i] in l2:
        print(l1[i], "-", l1.count(l1[i]),"times")
    else:
        l2.append(l1[i])