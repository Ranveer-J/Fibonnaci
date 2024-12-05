
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def print_fibonacci_sequence(terms):
    if terms <= 0:
        print("Number of terms must be a positive integer.")
        return
    print("Fibonacci sequence for" ,terms " terms:")
    for i in range(terms):
        print(fibonacci(i), end=" ")
    print()  



