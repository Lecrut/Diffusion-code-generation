def render_diamond_pattern(height):
    if height % 2 == 0:
        return ""
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
    return "\n".join(lines)

if __name__ == '__main__':
    print(render_diamond_pattern(7))