def generate_diamond_pattern(center_width=9):
    if center_width % 2 == 0:
        center_width += 1
    half = center_width // 2
    lines = []
    for i in range(-half, half + 1):
        space_count = half - abs(i)
        star_count = center_width - 2 * space_count
        line = ' ' * space_count + '*' * star_count
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_diamond_pattern(9)
    print(result)