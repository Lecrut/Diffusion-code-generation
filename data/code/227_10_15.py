def print_star_triangle(rows):
    if rows <= 0:
        raise ValueError("Number of rows must be a positive integer.")
    
    triangle_pattern = '\n'.join(['*' * i for i in range(1, rows + 1)])
    return triangle_pattern

if __name__ == '__main__':
    try:
        sample_rows = 5
        print(print_star_triangle(sample_rows))
    except ValueError as e:
        print(e)