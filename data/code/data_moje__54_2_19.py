def hollow_square(n):
    if n <= 0:
        return []
    if n == 1:
        return ['*']
    return ['*' + ' ' * (n - 2) + '*' if 0 < i < n - 1 else '*' * n for i in range(n)]

if __name__ == '__main__':
    print(hollow_square(5))