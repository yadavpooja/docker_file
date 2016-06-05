num = int(input("enter a number to find factorial: "))
result = 1
while num != 1:
    result *= num
    num -= 1

print "Factorial of give number is %d." %result
