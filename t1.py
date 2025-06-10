def fun():
    l= [5,7,0,1,4,3,6,2,8,9]
    d = {}
    for i in l:
        if i%2==0:
            d[i] = 'Even' 
        else :
            d[i] = 'Odd'
    return d
print(fun())

