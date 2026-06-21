def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

if __name__ == '__main__':
    sample_n = 10
    fib_value = fibonacci(sample_n)
    print(f"Fibonacci({sample_n}) = {fib_value}")