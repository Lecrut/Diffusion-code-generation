def generate_right_triangle(height):
    return '\n'.join([' '.join(map(str, range(1, i + 1))) for i in range(1, height + 1)])

if __name__ == '__main__':
    triangle = generate_right_triangle(5)
    print(triangle)