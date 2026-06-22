def fill_rectangle(width, height, char):
    return [([char] * width) for _ in range(height)]

if __name__ == '__main__':
    w = 5
    h = 3
    c = '*'
    rectangle = fill_rectangle(w, h, c)
    for row in rectangle:
        print(''.join(row))