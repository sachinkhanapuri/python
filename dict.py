#i/p :- {'A':1,'B':2,'C':3,'D':1}
# o/p :- {1:['A','D'],2:'B',3:'C'}

dict1={}
l=int(input("enter the length of dictonary:"))
for i in range(0,l):
    keys=input("enter the key value of dict:")
    values=input("enter the value of dict:")
    dict1.update({keys:values})
print("orignial dictonary :",dict1)

dict2={}
for keys,values in dict1.items():
    print(keys)
    print(values)
    dict2[values]=dict2.get(values,[])
    dict2[values].append(keys)
print("orignial dictonary :",dict1)
print("dictonary:",dict2)

            





