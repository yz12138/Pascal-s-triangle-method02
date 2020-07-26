# l1=[1,2,1]
#
# def tri(x):
#     l2=[]
#     for i in range(len(x)-1):
#         w2=x[i]+x[i+1]
#         l2.append(w2)
#     l2.insert(0,1)
#     l2.append(1)
#     return l2
# for temp in range(10):
#     print(l1)
#     l1=tri(l1)

def tri():
    l1=[1]
    while True:
        yield l1                            #yield 作用1,将tri函数转化为generator，作用2，用next()调用时，返回l1，相当于return l1
        if len(l1)==1:
            l1=[1,1]
        else:
            l1=[l1[i]+l1[i+1] for i,value in enumerate(l1) if i<len(l1)-1]
            l1.insert(0,1)
            l1.append(1)
    return 'done'
n=0
result=[]
for temp in tri():
    result.append(temp)
    n=n+1
    if n==5:
        break
for x in result:
    print(x)