def generate_triangle_pattern(height):
    return '\n'.join(['*' * (i + 1) for i in range(height)])

if __name__ == '__main__':
    sample_height = 7
    triangle = generate_triangle_pattern(sample_height)
    print(triangle)