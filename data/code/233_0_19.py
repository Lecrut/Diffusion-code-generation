def fill_rectangle():
    rectangle = [['*' for _ in range(5)] for _ in range(5)]
    return rectangle

if __name__ == '__main__':
    rectangle = fill_rectangle()
    for row in rectangle:
        print(''.join(row))