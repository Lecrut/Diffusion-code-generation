def print_symmetric_triangle(height):
    for i in range(1, height + 1):
        print(' ' * (height - i) + '*' * (2 * i - 1))

if __name__ == '__main__':
    print_symmetric_triangle(6)