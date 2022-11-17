def fonc(l1,l2):
    l3 = []
    cm = 0
    for i in l1:
        for j in l2:
            if(i == j):
                for t in l3:
                    if(t == i):
                        cm = 1
                if(cm == 0):
                    l3.append(i)
                cm = 0
    return l3

print(fonc([1,1,55,5],[5,55,68,1]))
                
