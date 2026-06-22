WIDTH = 6
HEIGHT = 4

def generate_hollow_rectangle(w, h):
    lines = []
    for i in range(h):
        if i == 0 or i == h - 1:
            line = "*" * w
        else:
            line = "*" + " " * (w - 2) + "*"
        lines.append(line)
    return lines

if __name__ == '__main__':
    pattern = generate_hollow_rectangle(WIDTH, HEIGHT)
    for line in pattern:
        print(line)