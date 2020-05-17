from math import*
def sequence(a,n,d):
    term=a+(n-1)*d
    return term
a=int(input("Enter first no"))
n=int(input("Enter the no of term"))
d=int(input("Enter the common difference"))
print("The nth term of sequence","is",sequence(a,n,d))

x=input("Do you want to continue or not?")
if(x=="yes"):
    a1 = a
    n1 = int(input("Enter the no of term"))
    d1 = d
    print("The nth term of sequence", "is", sequence(a, n, d))
else:
    print("the program is end")


