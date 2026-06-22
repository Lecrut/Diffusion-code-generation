WIDTH = 6
HEIGHT = 4

def generate_hollow_rectangle(width, height):
    lines = []
    for i in range(height):
        if i == 0 or i == height - 1:
            line = "*" * width
        else:
            line = "*" + " " * (width - 2) + "*"
        lines.append(line)
    return lines

if __name__ == '__main__':
    pattern = generate_hollow_rectangle(WIDTH, HEIGHT)
    for line in pattern:
        print(line)