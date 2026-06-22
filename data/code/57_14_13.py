def fib_sequence(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    dp = [0, 1]
    [dp.append(dp[-1] + dp[-2]) for _ in range(n - 2)]
    return dp

if __name__ == '__main__':
    limit = 15
    result = fib_sequence(limit)
    print(result)