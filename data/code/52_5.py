def render_diamond(rows):
    upper_range = (rows + 1) // 2
    lower_range = rows - upper_range
    lines = []
    for i in range(1, upper_range + 1):
        spaces = " " * (upper_range - i)
        stars = "* " * i
        lines.append(spaces + stars.strip())
    for i in range(lower_range, 0, -1):
        spaces = " " * (upper_range - i)
        stars = "* " * i
        lines.append(spaces + stars.strip())
    return "\n".join(lines)

if __name__ == '__main__':
    print(render_diamond(3))