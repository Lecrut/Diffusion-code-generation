def create_hollow_square(n):
    if n <= 0:
        return []
    if n == 1:
        return ['*']
    first_last = '*' * n
    middle = '*' + ' ' * (n - 2) + '*'
    lines = [first_last]
    if n > 2:
        lines += [middle] * (n - 2)
        lines.append(first_last)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(create_hollow_square(5))
    print(create_hollow_square(1))
    print(create_hollow_square(3))