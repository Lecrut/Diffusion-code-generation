def build_triangle_pattern(height):
    def validate_height(h):
        if not isinstance(h, int) or h <= 0:
            raise ValueError("Height must be a positive integer")
        return h

    validate_height(height)
    triangle_lines = []
    for row_num in range(1, height + 1):
        left_padding = ' ' * (height - row_num)
        star_segment = '*' * (2 * row_num - 1)
        triangle_lines.append(left_padding + star_segment)
    return '\n'.join(triangle_lines)

if __name__ == '__main__':
    sample_height = 7
    pattern_output = build_triangle_pattern(sample_height)
    print(pattern_output)