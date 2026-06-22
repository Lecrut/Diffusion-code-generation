def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    test_values = [0, 1, 2, 5, 10, 20]
    expected_results = [1, 1, 2, 120, 3628800, 2432902008176640000]
    for val, expected in zip(test_values, expected_results):
        computed = factorial(val)
        print(f"factorial({val}) = {computed}")
        assert computed == expected, f"Mismatch for {val}: got {computed}, expected {expected}"