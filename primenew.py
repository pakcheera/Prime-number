import numpy as np
A=list([])
def check(a):
    for i in range(2,int(np.sqrt(a))):
        if a%i == 0:
            return(0)
    return(a)
number = int(input('please input the number '))
for i in range(2,number+1):
    if check(i) !=  0 :
         A.append(check(i))
         print(i)
print(A)
for i in range(1,len(A)):
    if A[i]-A[i-1]==2:
        print(A[i-1],'and',A[i],'are twin prime')
