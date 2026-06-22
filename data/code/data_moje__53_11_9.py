def print_reverse_number_triangle(height):
    for i in range(height, 0, -1):
        print(str(i) * i)

if __name__ == '__main__':
    triangle_height = 5
    print_reverse_number_triangle(triangle_height)