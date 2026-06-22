def factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    test_cases = [0, 1, 5, 10, 15]
    for tc in test_cases:
        print(factorial(tc))