import random

l=["New York","Manhattan","Hongkong","Toronto","Vancouver"]
x=random.randint(0,len(l))

n="_"
z=len(l[x])
s=n*z
q=[]
t=5 
for i in range (0,z):
    q.append(n)

print(l[x])
print(q)


while t>0:
    print(" ".join(q))
    print("number of lives left: ",t)
    y=input("Enter a letter: ")
    
    if y in l[x]:
        print("correct answer")
        print("number of lives left: ",t)
        for j in range(0,z):
            if l[x][j]==y:
                q[j]=y
        if "".join(q)==l[x]:       
            print ("you won")
            t=0
    else:
        t=t-1
        print("wrong answer")
        if t==0:
            print("Better Luck Next Time")


