def generate_isosceles_triangle(rows: int) -> str:
    if rows <= 0:
        return ''
    max_width = 2 * rows - 1
    lines = []
    for i in range(1, rows + 1):
        spaces = (max_width - (2 * i - 1)) // 2
        stars = 2 * i - 1
        line = ' ' * spaces + '*' * stars
        lines.append(line)
    return '\n'.join(lines)
if __name__ == '__main__':
    sample_rows = 5
    print(generate_isosceles_triangle(sample_rows))