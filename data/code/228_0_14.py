def print_triangle(height):
    max_width = 2 * height - 1
    for i in range(height):
        spaces = max_width - (i * 2 + 1)
        asterisks = 2 * i + 1
        print(' ' * spaces // 2 + '*' * asterisks)

if __name__ == '__main__':
    triangle_height = 7
    print_triangle(triangle_height)