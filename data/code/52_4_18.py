def generate_diamond_star_pattern():
    center_width = 9
    half_height = (center_width - 1) // 2
    lines = []
    for i in range(half_height + 1):
        stars = 2 * i + 1
        spaces = half_height - i
        lines.append(' ' * spaces + '*' * stars)
    for i in range(half_height, 0, -1):
        stars = 2 * i - 1
        spaces = half_height - i + 1
        lines.append(' ' * spaces + '*' * stars)
    return lines

if __name__ == '__main__':
    print(generate_diamond_star_pattern())