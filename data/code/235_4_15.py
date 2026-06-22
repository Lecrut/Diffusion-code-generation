def generate_hollow_rectangle(width, height):
    if width < 2 or height < 2:
        raise ValueError("Width and height must be at least 2.")
    
    rectangle = []
    for i in range(height):
        if i == 0 or i == height - 1:
            line = "*" * width
        else:
            line = "*" + " " * (width - 2) + "*"
        rectangle.append(line)
    
    return rectangle

if __name__ == '__main__':
    WIDTH = 6
    HEIGHT = 4
    pattern = generate_hollow_rectangle(WIDTH, HEIGHT)
    for line in pattern:
        print(line)