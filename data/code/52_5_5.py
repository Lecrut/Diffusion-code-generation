def render_diamond(size):
    lines = []
    for i in range(size, 0, -1):
        spaces = ' ' * (size - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    upper = lines[:-1]
    lower = lines[::-1]
    result = upper + lower
    return '\n'.join(result)

if __name__ == '__main__':
    print(render_diamond(3))