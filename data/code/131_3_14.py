def factorial(n, memo={0: 1, 1: 1}):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n not in memo:
        memo[n] = n * factorial(n - 1, memo)
    return memo[n]

if __name__ == '__main__':
    test_value = 5
    result = factorial(test_value)
    print(f"Factorial of {test_value}: {result}")