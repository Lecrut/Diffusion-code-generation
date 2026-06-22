def print_equilateral_triangle(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

if __name__ == '__main__':
    triangle_height = 6
    print_equilateral_triangle(triangle_height)