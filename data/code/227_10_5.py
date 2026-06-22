def generate_star_triangle(num_rows):
    if not isinstance(num_rows, int) or num_rows <= 0:
        raise ValueError("Number of rows must be a positive integer")
    
    triangle_pattern = '\n'.join(['*' * i for i in range(1, num_rows + 1)])
    return triangle_pattern

if __name__ == '__main__':
    try:
        sample_value = 5
        print(generate_star_triangle(sample_value))
    except ValueError as e:
        print(e)