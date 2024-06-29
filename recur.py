def summ(n,sum):
    if n!=0:
     sum=sum+n
     return summ(n-1,sum) 
    return sum
sum=0    
print(summ(10,sum))
