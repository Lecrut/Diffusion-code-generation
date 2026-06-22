def print_diamond(size):
    lines = []
    for i in range(1, size + 1):
        line = ' ' * (size - i) + '*' * (2 * i - 1)
        lines.append(line)
    for i in range(size - 1, 0, -1):
        line = ' ' * (size - i) + '*' * (2 * i - 1)
        lines.append(line)
    return lines

if __name__ == '__main__':
    n = 8
    diamond_lines = print_diamond(n)
    for line in diamond_lines:
        print(line)