def print_star_triangle(height):
    for i in range(1, height + 1):
        print('*' * (2 * i - 1))
    for i in range(height - 1, 0, -1):
        print('*' * (2 * i - 1))

if __name__ == '__main__':
    print_star_triangle(6)