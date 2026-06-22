def create_triangle(height):
    for row in range(1, height + 1):
        print('*' * row)

if __name__ == '__main__':
    TRIANGLE_ROWS = 5
    create_triangle(TRIANGLE_ROWS)