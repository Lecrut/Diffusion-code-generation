def generate_isosceles_triangle(rows):
    lines = []
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    return '\n'.join(lines)
if __name__ == '__main__':
    sample_rows = 5
    triangle_pattern = generate_isosceles_triangle(sample_rows)
    print(triangle_pattern)