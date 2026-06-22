def factorial(n):
    if n < 0:
        raise ValueError("Input must be non-negative")
    result = 1
    i = 2
    while i <= n:
        result *= i
        i += 1
    return result

if __name__ == '__main__':
    print(factorial(0))
    print(factorial(5))
    print(factorial(10))