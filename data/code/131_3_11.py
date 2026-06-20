def factorial(n, memo={0: 1, 1: 1}):
    if n not in memo:
        memo[n] = n * factorial(n - 1, memo)
    return memo[n]

if __name__ == '__main__':
    test_value_1 = 5
    result_1 = factorial(test_value_1)
    print(f"Factorial of {test_value_1}: {result_1}")
    
    test_value_2 = 7
    result_2 = factorial(test_value_2)
    print(f"Factorial of {test_value_2}: {result_2}")