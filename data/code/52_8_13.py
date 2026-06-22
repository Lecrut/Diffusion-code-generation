def render_diamond(height):
    middle = height // 2 + 1
    lines = []
    for i in range(1, middle + 1):
        spaces = ' ' * (middle - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    for i in range(middle - 1, 0, -1):
        spaces = ' ' * (middle - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = render_diamond(7)
    print(result)