def print_pyramid_line(n):
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

if __name__ == '__main__':
    print_pyramid_line(5)