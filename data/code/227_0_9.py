def print_right_triangle(height):
    for row in range(1, height + 1):
        for col in range(row):
            print('*', end='')
        print()

if __name__ == '__main__':
    triangle_height = 5
    print_right_triangle(triangle_height)