def fibonacci(n, memo={}):
    if n < 0:
        raise ValueError('Input must be a non-negative integer.')
    elif n in memo:
        return memo[n]
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        return memo[n]
if __name__ == '__main__':
    print(fibonacci(10))
    print(fibonacci(1))
    print(fibonacci(8))