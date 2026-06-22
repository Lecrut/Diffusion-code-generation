def fill_and_print_rectangle():
    rectangle = [['*' for _ in range(5)] for _ in range(5)]
    for row in rectangle:
        print(' '.join(row))

if __name__ == '__main__':
    fill_and_print_rectangle()