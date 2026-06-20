def factorial(n, memo={}):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0 or n == 1:
        return 1
    if n not in memo:
        memo[n] = n * factorial(n - 1)
    return memo[n]

if __name__ == '__main__':
    print(factorial(5))