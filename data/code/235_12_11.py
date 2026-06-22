def print_pyramid_line(char, width):
    for i in range(width):
        spaces = ' ' * (width - i - 1)
        stars = char * (2 * i + 1)
        print(spaces + stars)

if __name__ == '__main__':
    print_pyramid_line('*', 5)