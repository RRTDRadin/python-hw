def prints(n):
    if(n<=0):
        return
    print("Codingal")
    prints(n/2)
    prints(n/2)
n=int(input("Enter your number: "))
prints(n)