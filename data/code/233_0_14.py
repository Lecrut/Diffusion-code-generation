def generate_asterisk_rectangle(width, height):
    return [['*' for _ in range(width)] for _ in range(height)]

if __name__ == '__main__':
    w = 5
    h = 3
    rectangle = generate_asterisk_rectangle(w, h)
    for row in rectangle:
        print(''.join(row))