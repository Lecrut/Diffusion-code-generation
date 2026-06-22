def compute_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    counter = 2
    while counter <= n:
        result *= counter
        counter += 1
    return result

if __name__ == '__main__':
    sample_value = 5
    factorial_result = compute_factorial(sample_value)
    print(factorial_result)