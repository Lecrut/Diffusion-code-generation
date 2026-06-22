def factorial(n):
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers")
    if n <= 1:
        return 1
    acc = 1
    idx = 2
    while idx <= n:
        acc *= idx
        idx += 1
    return acc

if __name__ == '__main__':
    print(factorial(0))
    print(factorial(1))
    print(factorial(5))
    print(factorial(10))
    print(factorial(3))