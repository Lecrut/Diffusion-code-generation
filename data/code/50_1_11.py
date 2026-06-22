def print_isosceles_triangle(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

if __name__ == '__main__':
    print_isosceles_triangle(7)