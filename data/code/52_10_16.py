def generate_diamond(n):
    if n <= 0:
        return ''
    lines = []
    for i in range(1, n + 1):
        stars = 2 * i - 1
        spaces = n - i
        line = ' ' * spaces + '*' * stars + ' ' * spaces
        lines.append(line)
    for i in range(n - 1, 0, -1):
        stars = 2 * i - 1
        spaces = n - i
        line = ' ' * spaces + '*' * stars + ' ' * spaces
        lines.append(line)
    return '\n'.join(lines)
if __name__ == '__main__':
    print(generate_diamond(5))