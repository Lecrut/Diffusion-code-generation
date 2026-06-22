def generate_hollow_rectangle(width, height):
    pattern = []
    for i in range(height):
        if i == 0 or i == height - 1:
            line = "*" * width
        else:
            line = "*" + " " * (width - 2) + "*"
        pattern.append(line)
    return pattern

if __name__ == '__main__':
    WIDTH = 6
    HEIGHT = 4
    pattern = generate_hollow_rectangle(WIDTH, HEIGHT)
    for line in pattern:
        print(line)