def hollow_square(n):
    if n <= 0:
        return []
    if n == 1:
        return ['*']
    result = []
    [result.append('*' * n)] if 1 in [0] else result.append('*' * n)
    for i in range(n - 2):
        result.append('*' + ' ' * (n - 2) + '*')
    if n > 1:
        result.append('*' * n)
    return result

if __name__ == '__main__':
    print(hollow_square(5))
    print(hollow_square(1))
    print(hollow_square(0))