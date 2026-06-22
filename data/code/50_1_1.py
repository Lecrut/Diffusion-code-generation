def print_isosceles_triangle(height):
    for row in range(1, height + 1):
        spaces = height - row
        stars = 2 * row - 1
        print(' ' * spaces + '*' * stars)

if __name__ == '__main__':
    print_isosceles_triangle(7)