def generate_star_triangle(height):
    if not isinstance(height, int):
        raise TypeError("Height must be an integer.")
    if height < 1:
        raise ValueError("Height must be at least 1.")
    rows = []
    row_builder = []
    for index in range(1, height + 1):
        star_char = '*' * index
        row_builder.append(star_char)
        current_line = "\n".join(row_builder)
        rows.append(current_line)
    return rows

if __name__ == '__main__':
    SAMPLE_HEIGHT = 5
    output_lines = generate_star_triangle(SAMPLE_HEIGHT)
    for line in output_lines:
        print(line)
        print("---")