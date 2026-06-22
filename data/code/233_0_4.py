def fill_rectangle(height=5, width=5, char='*'):
    return [[char for _ in range(width)] for _ in range(height)]

if __name__ == '__main__':
    rectangle = fill_rectangle()
    for row in rectangle:
        print(''.join(row))