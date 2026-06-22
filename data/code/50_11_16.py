def build_row_template(width, center):
    left_pad = (width - center) // 2
    right_pad = width - left_pad - center
    return left_pad * ' ' + '*' * center + right_pad * ' '

def generate_isosceles_triangle(rows):
    if rows <= 0:
        return ''
    max_width = 2 * rows - 1
    star_counts = {i: 2 * i - 1 for i in range(1, rows + 1)}
    line_builder = [build_row_template(max_width, star_counts[i]) for i in range(1, rows + 1)]
    joined_lines = '\n'.join(line_builder)
    return joined_lines

if __name__ == '__main__':
    sample_rows = 5
    result = generate_isosceles_triangle(sample_rows)
    print(result)