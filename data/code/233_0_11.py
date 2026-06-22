def fill_rectangle(width=5, height=5, char='*'):
    if not all(isinstance(i, int) and i > 0 for i in [width, height]):
        raise ValueError("Width and height must be positive integers")
    return [[char for _ in range(width)] for _ in range(height)]

if __name__ == '__main__':
    rectangle = fill_rectangle()
    for row in rectangle:
        print(''.join(row))