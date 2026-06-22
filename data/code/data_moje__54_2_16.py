def hollow_square(n):
    if n <= 0:
        return []
    if n == 1:
        return ['*']
    if n == 2:
        return ['**', '**']
    top_bottom = '*' * n
    middle = '*' + ' ' * (n - 2) + '*'
    return [top_bottom] + [middle] * (n - 2) + [top_bottom]

if __name__ == '__main__':
    n = 5
    result = hollow_square(n)
    for line in result:
        print(line)