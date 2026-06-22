def generate_diamond_pattern(center_width):
    if center_width % 2 == 0:
        center_width += 1
    max_stars = center_width
    half_height = (max_stars + 1) // 2
    lines = []
    lines.extend(
        ' ' * (half_height - i) + '*' * (2 * i - 1)
        for i in range(1, half_height)
    )
    lines.append('*' * max_stars)
    lines.extend(
        ' ' * (half_height - i) + '*' * (2 * i - 1)
        for i in range(half_height - 1, 0, -1)
    )
    return '\n'.join(lines)

if __name__ == '__main__':
    width = 9
    result = generate_diamond_pattern(width)
    print(result)