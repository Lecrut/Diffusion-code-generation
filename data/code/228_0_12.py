def print_triangle(height):
    max_width = 2 * height - 1
    for i in range(1, height + 1):
        spaces = max_width - 2 * i
        asterisks = 2 * i - 1
        print(' ' * (spaces // 2) + '*' * asterisks)

if __name__ == '__main__':
    print_triangle(5)