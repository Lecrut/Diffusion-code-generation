def render_diamond(height):
    lines = []
    for i in range(1, height + 1):
        line = ' ' * (height - i) + '*' * (2 * i - 1)
        lines.append(line)
    for i in range(height - 1, 0, -1):
        line = ' ' * (height - i) + '*' * (2 * i - 1)
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = render_diamond(7)
    print(result)