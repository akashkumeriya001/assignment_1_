n = int(input("Enter the number "))
n1,n2 = 0,1
count = 0
if n <= 0:
    print("please enter positive number")
elif n == 1:
    print("Fibonacci sequence upto",n,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < n:
        print (n1)
        r = n1 + n2
        n1 = n2
        n2 = r
        count += 1