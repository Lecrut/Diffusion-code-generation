def print_pyramid():
    base_width = 21
    height = (base_width + 1) // 2
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

if __name__ == '__main__':
    print_pyramid()