def render_diamond():
    size = 3
    lines = []
    for i in range(size):
        spaces = ' ' * (size - 1 - i)
        stars = '*' * (2 * i + 1)
        lines.append(spaces + stars)
    for i in range(size - 2, -1, -1):
        spaces = ' ' * (size - 1 - i)
        stars = '*' * (2 * i + 1)
        lines.append(spaces + stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(render_diamond())