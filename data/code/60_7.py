def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    print(factorial(0))
    print(factorial(1))
    print(factorial(5))
    print(factorial(10))
    try:
        factorial(-1)
    except ValueError as e:
        print(str(e))
    try:
        factorial(3.5)
    except TypeError as e:
        print(str(e))