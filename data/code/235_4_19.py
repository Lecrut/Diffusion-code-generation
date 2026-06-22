def generate_hollow_rectangle(width, height):
    pattern = []
    for i in range(height):
        if i == 0 or i == height - 1:
            pattern.append('*' * width)
        else:
            line = '*' + ' ' * (width - 2) + '*'
            pattern.append(line)
    return pattern

if __name__ == '__main__':
    WIDTH = 6
    HEIGHT = 4
    rectangle_pattern = generate_hollow_rectangle(WIDTH, HEIGHT)
    for row in rectangle_pattern:
        print(row)