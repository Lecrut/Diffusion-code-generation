def create_triangle(height):
    for level in range(1, height + 1):
        print('*' * level)

if __name__ == '__main__':
    TRIANGLE_HEIGHT = 7
    create_triangle(TRIANGLE_HEIGHT)