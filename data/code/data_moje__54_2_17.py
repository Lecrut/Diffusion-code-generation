def create_hollow_square(n):
    if n <= 0:
        return []
    if n == 1:
        return ['*']
    top_bottom = '*' * n
    middle = '*' + ' ' * (n - 2) + '*'
    return [top_bottom] + [middle] * (n - 2) + [top_bottom]

if __name__ == '__main__':
    print(create_hollow_square(5))
    print(create_hollow_square(1))
    print(create_hollow_square(2))