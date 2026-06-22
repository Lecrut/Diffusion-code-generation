def create_rectangle(width, height, char):
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers.")
    return [[char for _ in range(width)] for _ in range(height)]

if __name__ == '__main__':
    w = 5
    h = 5
    c = '*'
    rectangle = create_rectangle(w, h, c)
    for row in rectangle:
        print(''.join(row))