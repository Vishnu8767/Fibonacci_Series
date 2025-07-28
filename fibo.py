# Number of terms
n = int(input("Enter how many Fibonacci numbers you want: "))

# First two terms
a, b = 0, 1

print("Fibonacci Sequence:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

