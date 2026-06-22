def compute_factorial(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

if __name__ == '__main__':
    sample_value = 5
    print(compute_factorial(sample_value))