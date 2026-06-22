def print_centered_triangle(levels):
    for i in range(levels):
        spaces = ' ' * (levels - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

if __name__ == '__main__':
    print_centered_triangle(12)