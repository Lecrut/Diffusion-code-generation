def print_inverted_right_triangle(rows):
    for i in range(rows, 0, -1):
        print('*' * i)

if __name__ == '__main__':
    triangle_height = 6
    print_inverted_right_triangle(triangle_height)