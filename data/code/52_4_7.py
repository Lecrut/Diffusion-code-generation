def generate_diamond_pattern(center_width=9):
    if center_width % 2 == 0:
        center_width += 1
    max_width = center_width
    half = center_width // 2
    upper_lines = []
    for i in range(half + 1):
        stars_count = 2 * i + 1
        spaces_count = (max_width - stars_count) // 2
        line = ' ' * spaces_count + '*' * stars_count
        upper_lines.append(line)
    lower_lines = upper_lines[:-1][::-1]
    full_pattern = upper_lines + lower_lines
    return full_pattern

if __name__ == '__main__':
    result = generate_diamond_pattern(9)
    for line in result:
        print(line)