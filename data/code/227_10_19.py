def print_star_triangle(rows):
    if rows < 1:
        raise ValueError("Number of rows must be at least 1")
    
    triangle_pattern = '\n'.join(['*' * i for i in range(1, rows + 1)])
    return triangle_pattern

if __name__ == '__main__':
    sample_rows = 5
    try:
        pattern = print_star_triangle(sample_rows)
        print(pattern)
    except ValueError as e:
        print(e)