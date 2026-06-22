def validate_rows(rows):
    if not isinstance(rows, int):
        raise TypeError("rows must be an integer")
    if rows < 1:
        raise ValueError("rows must be positive")

def generate_left_aligned_triangle(rows):
    validate_rows(rows)
    result_lines = []
    for i in range(1, rows + 1):
        result_lines.append('*' * i)
    return '\n'.join(result_lines)

if __name__ == '__main__':
    ROW_COUNT = 15
    triangle_output = generate_left_aligned_triangle(ROW_COUNT)
    print(triangle_output)