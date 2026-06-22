def print_equilateral_triangle(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        asterisks = '*' * (2 * i - 1)
        print(spaces + asterisks)

if __name__ == '__main__':
    triangle_height = 5
    print_equilateral_triangle(triangle_height)