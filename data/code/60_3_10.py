def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    test_cases = [0, 1, 5, 10, 20, 50, 100]
    expected_results = [1, 1, 120, 3628800, 2432902008176640000, 30414093201713378043612608166064768844377641568960512000000000000, 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000]
    for i, n in enumerate(test_cases):
        result = factorial(n)
        print(f"factorial({n}) = {result}")
        assert result == expected_results[i], f"Expected {expected_results[i]}, got {result}"