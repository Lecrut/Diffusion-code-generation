def generate_pyramid_pattern(height=5):
    lines = []
    max_width = 2 * height - 1
    for row in range(1, height + 1):
        number_part = str(row) * (2 * row - 1)
        padding = (max_width - len(number_part)) // 2
        line = ' ' * padding + number_part + ' ' * padding
        lines.append(line)
    return '\n'.join(lines)

def print_pyramid_pattern():
    pattern = generate_pyramid_pattern(5)
    print(pattern)
    return pattern
if __name__ == '__main__':
    print_pyramid_pattern()