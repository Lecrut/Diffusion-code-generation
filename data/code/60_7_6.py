def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    print(factorial(5))
    print(factorial(0))
    try:
        print(factorial(-3))
    except ValueError as e:
        print(e)
    try:
        print(factorial("a"))
    except TypeError as e:
        print(e)