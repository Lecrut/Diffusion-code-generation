def generate_diamond(n):
    lines = []
    for i in range(1, n + 1):
        lines.append(' ' * (n - i) + '*' * (2 * i - 1))
    for i in range(n - 1, 0, -1):
        lines.append(' ' * (n - i) + '*' * (2 * i - 1))
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_diamond(5))