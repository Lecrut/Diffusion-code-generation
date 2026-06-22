def create_rectangle(width, height, char):
    return [[char for _ in range(width)] for _ in range(height)]

if __name__ == '__main__':
    w = 5
    h = 3
    c = '#'
    rectangle = create_rectangle(w, h, c)
    for row in rectangle:
        print(''.join(row))