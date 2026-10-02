# Write a program which gets a positive integer from a user using input() and assigns it to a variable.
num = n = int(input("Enter a positive integer: "))
result = 0

while num >= 1:
    result += num
    num -= 1

print("User entered: " + str(n))
print("Sum of integers: " + str(result))