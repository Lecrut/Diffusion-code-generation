def factorial_while(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    result = 1
    current = 1
    while current <= n:
        result *= current
        current += 1
    return result

if __name__ == '__main__':
    print(factorial_while(0))
    print(factorial_while(5))
    print(factorial_while(10))