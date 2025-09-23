def path(adj,set,arr,sum,list):
    for i in adj:
        if(i[0] not in set):
            sum+=i[1]
            set.add(i[0])
            arr.append(i[0])
            if(i[0]=='D' and len(set)==4):
                print(str(arr)+" "+str(sum))
                sum+=4
                arr.append('A')
                print(str(arr)+" "+str(sum))
                sum-=4
                arr.pop()
            else:
                path(list[i[0]],set,arr,sum,list)
            sum-=i[1]
            set.remove(i[0])
            arr.pop()
list={
    'A':[('B',2),('D',4)],
    'B':[('C',3),('A',2)],
    'C':[('B',3),('D',1)],
    'D':[('A',4),('C',1)]
    }
set=set()
set.add('A')
arr=['A']
path(list['A'],set,arr,0,list)

