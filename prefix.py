def prefix_adder(firstlist):
    secondlist=[]
    for i in firstlist:
        if(len(i)>0):
            secondlist.append("Dr."+i)
    return secondlist
firstlist = ["Phil","Oz","Suess","Dre"]
print(prefix_adder(firstlist))