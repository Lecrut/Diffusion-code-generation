def fibonacci(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

if __name__ == '__main__':
    nth_fibonacci = fibonacci(10)
    print(nth_fibonacci)