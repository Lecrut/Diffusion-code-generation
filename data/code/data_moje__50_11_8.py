def generate_isosceles_triangle(rows):
    if rows <= 0:
        return ''
    SPACING = ' '
    STAR = '*'
    lines = []
    for current_row in range(1, rows + 1):
        prefix_length = rows - current_row
        star_count = 2 * current_row - 1
        line_content = SPACING * prefix_length + STAR * star_count
        lines.append(line_content)
    return '\n'.join(lines)

if __name__ == '__main__':
    SAMPLE_ROWS = 5
    triangle_output = generate_isosceles_triangle(SAMPLE_ROWS)
    print(triangle_output)