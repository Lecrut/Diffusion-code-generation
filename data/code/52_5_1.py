def render_diamond(size=3):
    lines = []
    for i in range(1, size + 1):
        line = ' ' * (size - i) + '*' * (2 * i - 1)
        lines.append(line)
    for i in range(size - 1, 0, -1):
        line = ' ' * (size - i) + '*' * (2 * i - 1)
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(render_diamond(3))