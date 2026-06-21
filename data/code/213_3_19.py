def fibonacci(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

if __name__ == '__main__':
    print(fibonacci(10))