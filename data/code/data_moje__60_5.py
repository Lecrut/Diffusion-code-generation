def compute_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    while n > 1:
        result = result * n
        n = n - 1
    return result

if __name__ == '__main__':
    sample_value = 5
    print(compute_factorial(sample_value))
    print(compute_factorial(0))
    print(compute_factorial(10))