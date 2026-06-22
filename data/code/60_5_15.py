def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    i = 1
    while i <= n:
        result = result * i
        i = i + 1
    return result

if __name__ == '__main__':
    print(factorial(5))
    print(factorial(0))
    print(factorial(10))