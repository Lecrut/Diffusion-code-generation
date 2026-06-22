def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    sample_values = [0, 1, 5, 10]
    for val in sample_values:
        print(factorial(val))