def fill_rectangle(width, height):
    return [['*' for _ in range(width)] for _ in range(height)]

if __name__ == '__main__':
    width = 5
    height = 5
    rectangle = fill_rectangle(width, height)
    for row in rectangle:
        print(''.join(row))