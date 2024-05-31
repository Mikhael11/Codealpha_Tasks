def fab(n):
    if n <= 1:
        return n
    else:
        return fab(n-1) + fab(n-2)
    


num =int(input("Enter a Positive number : "))
if num <= 0:
    print("Enter a positive number!!: ")
else:
    print ("Fabbonacci series :" )
    for i in range(num):
        print(fab(i))
        print()