def generate_right_triangle(height):
    return '\n'.join(['*' * (i + 1) for i in range(height)])

if __name__ == '__main__':
    print(generate_right_triangle(5))