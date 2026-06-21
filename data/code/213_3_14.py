def fibonacci_memo(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

if __name__ == '__main__':
    sample_n = 15
    result = [fibonacci_memo(i) for i in range(sample_n)]
    print(result)