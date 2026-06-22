def make_diamond(radius):
    lines = []
    for i in range(1, radius + 1):
        lines.append(' ' * (radius - i) + '*' * (2 * i - 1))
    for i in range(radius - 1, 0, -1):
        lines.append(' ' * (radius - i) + '*' * (2 * i - 1))
    return '\n'.join(lines)

if __name__ == '__main__':
    print(make_diamond(5))