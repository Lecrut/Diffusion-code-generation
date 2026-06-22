def generate_right_triangle(height):
    return '\n'.join(['*' * (i + 1) for i in range(height)])

if __name__ == '__main__':
    triangle = generate_right_triangle(5)
    print(triangle)