def create_right_triangle(height):
    return '\n'.join(['*' * (i + 1) for i in range(height)])

if __name__ == '__main__':
    print(create_right_triangle(5))