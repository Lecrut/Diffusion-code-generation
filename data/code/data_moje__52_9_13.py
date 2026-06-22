def generate_diamond_pattern(half_height):
    lines = []
    for i in range(1, half_height + 1):
        spaces = ' ' * (half_height - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    for i in range(half_height - 1, 0, -1):
        spaces = ' ' * (half_height - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    return lines
if __name__ == '__main__':
    half_height = 4
    diamond_lines = generate_diamond_pattern(half_height)
    for line in diamond_lines:
        print(line)