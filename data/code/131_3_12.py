def factorial(n, memo={0: 1, 1: 1}):
    if n in memo:
        return memo[n]
    result = n * factorial(n - 1, memo)
    memo[n] = result
    return result

if __name__ == '__main__':
    test_value = 5
    print(factorial(test_value))