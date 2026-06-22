def generate_hollow_rectangle(width, height):
    if width < 2 or height < 2:
        return []

    rectangle = []
    for i in range(height):
        if i == 0 or i == height - 1:
            rectangle.append('*' * width)
        else:
            rectangle.append('*' + ' ' * (width - 2) + '*')
    return rectangle

if __name__ == '__main__':
    WIDTH = 6
    HEIGHT = 4
    pattern = generate_hollow_rectangle(WIDTH, HEIGHT)
    for line in pattern:
        print(line)