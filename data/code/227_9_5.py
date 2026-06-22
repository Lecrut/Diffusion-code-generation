def print_right_triangle(height):
    for i in range(1, height + 1):
        row = '*' * i
        print(row)

if __name__ == '__main__':
    triangle_height = 4
    print_right_triangle(triangle_height)