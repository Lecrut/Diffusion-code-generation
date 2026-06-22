def factorial(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    print(factorial(0))
    print(factorial(5))
    print(factorial(10))