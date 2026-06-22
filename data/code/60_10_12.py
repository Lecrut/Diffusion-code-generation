def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == '__main__':
    test_values = [0, 1, 5, 10]
    for value in test_values:
        print(factorial(value))
    try:
        factorial(-3)
    except ValueError as e:
        print(e)
    try:
        factorial(3.5)
    except TypeError as e:
        print(e)