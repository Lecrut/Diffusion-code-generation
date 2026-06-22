def print_diamond(n):
    lines = []
    for i in range(1, n + 1):
        line = ' ' * (n - i) + '*' * (2 * i - 1)
        lines.append(line)
    for i in range(n - 1, 0, -1):
        line = ' ' * (n - i) + '*' * (2 * i - 1)
        lines.append(line)
    return '\n'.join(lines)
if __name__ == '__main__':
    n = 5
    result = print_diamond(n)
    print(result)