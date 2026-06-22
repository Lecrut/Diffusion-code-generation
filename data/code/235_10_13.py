def generate_right_triangle(height):
    return '\n'.join(['*' * (i + 1) for i in range(height)])

if __name__ == '__main__':
    triangle_height = 7
    result = generate_right_triangle(triangle_height)
    print(result)