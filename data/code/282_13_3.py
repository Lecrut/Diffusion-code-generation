def total_recursive_memo(n, memo={}):
    if n == 0:
        return 0
    if n in memo:
        return memo[n]
    memo[n] = n + total_recursive_memo(n - 1)
    return memo[n]

if __name__ == '__main__':
    print(total_recursive_memo(5))