def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    current = 1
    while current <= n:
        result *= current
        current += 1
    return result

if __name__ == '__main__':
    sample_value = 5
    print(factorial(sample_value))
    sample_value = 0
    print(factorial(sample_value))
    sample_value = 7
    print(factorial(sample_value))