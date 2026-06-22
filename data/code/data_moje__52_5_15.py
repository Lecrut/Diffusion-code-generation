def render_diamond(size=3):
    lines = []
    for i in range(1, size + 1):
        spaces = ' ' * (size - i)
        stars = '* ' * i
        lines.append(spaces + stars.strip())
    for i in range(size - 1, 0, -1):
        spaces = ' ' * (size - i)
        stars = '* ' * i
        lines.append(spaces + stars.strip())
    return '\n'.join(lines)

if __name__ == '__main__':
    print(render_diamond())