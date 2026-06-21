def fibonacci(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

if __name__ == '__main__':
    sample_n = 10
    result = [fibonacci(i) for i in range(sample_n)]
    print(f"Fibonacci sequence up to {sample_n} terms: {result}")