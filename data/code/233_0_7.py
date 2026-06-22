def generate_rectangle(width, height, char):
    return [[char for _ in range(width)] for _ in range(height)]

if __name__ == '__main__':
    rect_width = 5
    rect_height = 4
    fill_char = '@'
    rectangle = generate_rectangle(rect_width, rect_height, fill_char)
    for row in rectangle:
        print(''.join(row))