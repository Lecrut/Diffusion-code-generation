def factorial(n, memo={0: 1, 1: 1}):
    if n not in memo:
        memo[n] = n * factorial(n - 1, memo)
    return memo[n]

if __name__ == '__main__':
    sample_value = 5
    result = factorial(sample_value)
    print(result)