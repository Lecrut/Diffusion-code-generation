def render_diamond(height):
    if height < 1 or height % 2 == 0:
        return []
    middle = height // 2
    lines = []
    for i in range(middle + 1):
        spaces = " " * (middle - i)
        stars = "*" * (2 * i + 1)
        lines.append(spaces + stars)
    for i in range(middle - 1, -1, -1):
        spaces = " " * (middle - i)
        stars = "*" * (2 * i + 1)
        lines.append(spaces + stars)
    return lines

if __name__ == '__main__':
    result = render_diamond(7)
    for line in result:
        print(line)