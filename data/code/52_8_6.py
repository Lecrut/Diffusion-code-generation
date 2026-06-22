def render_diamond(height):
    if height % 2 == 0:
        raise ValueError('Height must be an odd number')
    mid = height // 2
    lines = []
    for i in range(mid + 1):
        spaces = ' ' * (mid - i)
        stars = '*' * (2 * i + 1)
        lines.append(spaces + stars)
    for i in range(mid - 1, -1, -1):
        spaces = ' ' * (mid - i)
        stars = '*' * (2 * i + 1)
        lines.append(spaces + stars)
    return '\n'.join(lines)
if __name__ == '__main__':
    diamond_height = 7
    result = render_diamond(diamond_height)
    print(result)