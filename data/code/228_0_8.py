def print_triangle(height):
    max_width = 2 * height - 1
    for i in range(1, height + 1):
        spaces = ' ' * (max_width - 2 * i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

if __name__ == '__main__':
    triangle_height = 5
    print_triangle(triangle_height)