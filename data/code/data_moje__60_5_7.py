def compute_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    counter = 1
    while counter <= n:
        result *= counter
        counter += 1
    return result

if __name__ == '__main__':
    sample_value_1 = 5
    sample_value_2 = 0
    print(compute_factorial(sample_value_1))
    print(compute_factorial(sample_value_2))