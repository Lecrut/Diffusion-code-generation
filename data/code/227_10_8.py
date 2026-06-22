def validate_rows(rows):
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("Number of rows must be a positive integer")

def print_star_triangle(rows):
    validate_rows(rows)
    triangle_pattern = '\n'.join(['*' * i for i in range(1, rows + 1)])
    return triangle_pattern

if __name__ == '__main__':
    sample_rows = 5
    result = print_star_triangle(sample_rows)
    print(result)