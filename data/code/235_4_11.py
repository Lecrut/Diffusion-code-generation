def generate_hollow_rectangle(width, height):
    rectangle = []
    for i in range(height):
        if i == 0 or i == height - 1:
            row = '*' * width
        else:
            row = '*' + ' ' * (width - 2) + '*'
        rectangle.append(row)
    return rectangle

if __name__ == '__main__':
    WIDTH = 6
    HEIGHT = 4
    pattern = generate_hollow_rectangle(WIDTH, HEIGHT)
    for line in pattern:
        print(line)