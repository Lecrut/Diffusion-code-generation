def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

if __name__ == '__main__':
    print(factorial(0))
    print(factorial(1))
    print(factorial(5))
    print(factorial(10))