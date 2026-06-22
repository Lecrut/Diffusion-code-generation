def print_pyramid():
    width = 21
    for i in range(1, width + 1, 2):
        spaces = (width - i) // 2
        stars = '*' * i
        print(' ' * spaces + stars)

if __name__ == '__main__':
    print_pyramid()