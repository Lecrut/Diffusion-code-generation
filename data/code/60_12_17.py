def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    print(factorial(5))
    print(factorial(0))
    print(factorial(1))
    print(factorial(10))
    try:
        print(factorial(-1))
    except ValueError as e:
        print(e)
    try:
        print(factorial(5.5))
    except TypeError as e:
        print(e)