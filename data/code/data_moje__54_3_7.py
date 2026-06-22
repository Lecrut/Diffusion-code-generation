def hollow_square(n, border='#'):
    if n <= 0:
        return ''
    if n == 1:
        return border
    lines = []
    first_last = border * n
    middle = border + ' ' * (n - 2) + border
    lines.append(first_last)
    for _ in range(n - 2):
        lines.append(middle)
    lines.append(first_last)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(hollow_square(5))
    print(hollow_square(1))
    print(hollow_square(4, '*'))