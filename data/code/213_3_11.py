def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

if __name__ == '__main__':
    try:
        term = 10
        fib_value = fibonacci(term)
        print(f"Fibonacci({term}) = {fib_value}")
    except Exception as e:
        print(e)