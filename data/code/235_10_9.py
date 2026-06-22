def create_right_triangle(height):
    lines = ['*' * (i + 1) for i in range(height)]
    return '\n'.join(lines)

if __name__ == '__main__':
    triangle_height = 7
    triangle = create_right_triangle(triangle_height)
    print(triangle)