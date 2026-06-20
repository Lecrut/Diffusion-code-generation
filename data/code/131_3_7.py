def factorial(n, memo={}):
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    result = n * factorial(n - 1, memo)
    memo[n] = result
    return result
if __name__ == '__main__':
    print(factorial(5))