def diamond(r):
    lines = []
    for i in range(1, r + 1):
        lines.append(' ' * (r - i) + '*' * (2 * i - 1))
    for i in range(r - 1, 0, -1):
        lines.append(' ' * (r - i) + '*' * (2 * i - 1))
    return '\n'.join(lines)

if __name__ == '__main__':
    print(diamond(5))