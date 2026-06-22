def generate_triangle(height):
    return '\n'.join([' ' * (height - i - 1) + '*' * (2 * i + 1) for i in range(height)])

if __name__ == '__main__':
    triangle = generate_triangle(5)
    print(triangle)