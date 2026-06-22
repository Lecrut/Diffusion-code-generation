def hollow_square(n):
    if n <= 0:
        return []
    if n == 1:
        return ['*']
    row_first_last = '*' * n
    row_inner = '*' + ' ' * (n - 2) + '*'
    return [row_first_last] + [row_inner for _ in range(n - 2)] + [row_first_last]

if __name__ == '__main__':
    result = hollow_square(5)
    for line in result:
        print(line)