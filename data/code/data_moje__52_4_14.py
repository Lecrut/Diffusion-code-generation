def generate_diamond_pattern(center_width):
    half = center_width // 2
    lines = []
    for i in range(center_width):
        stars = 1 + 2 * i if i <= half else 1 + 2 * (center_width - 1 - i)
        spaces = half - i if i <= half else i - half
        line = ' ' * spaces + '*' * stars
        lines.append(line)
    return lines

def get_diamond_pattern_as_string(pattern_lines):
    return '\n'.join(pattern_lines)

if __name__ == '__main__':
    center_width = 9
    pattern_lines = generate_diamond_pattern(center_width)
    diamond_string = get_diamond_pattern_as_string(pattern_lines)
    print(diamond_string)