def generate_diamond_pattern(center_width=9):
    if center_width % 2 == 0:
        center_width += 1
    half = center_width // 2
    lines = []
    for i in range(-half, half + 1):
        spaces = ' ' * abs(i)
        stars = '*' * (center_width - 2 * abs(i))
        lines.append(spaces + stars)
    return lines

if __name__ == '__main__':
    pattern = generate_diamond_pattern(9)
    for line in pattern:
        print(line)