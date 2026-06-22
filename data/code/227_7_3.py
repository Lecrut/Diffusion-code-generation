def print_inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

if __name__ == '__main__':
    print_inverted_pyramid(5)