def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    test_cases = [0, 1, 5, 10, 20, 100]
    for n in test_cases:
        print(f"factorial({n}) = {factorial(n)}")