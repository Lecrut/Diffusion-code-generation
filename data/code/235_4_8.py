def generate_hollow_rectangle(width, height):
    if width < 2 or height < 2:
        raise ValueError("Width and height must be at least 2.")
    
    rectangle = []
    for y in range(height):
        line = ""
        for x in range(width):
            if y == 0 or y == height - 1 or x == 0 or x == width - 1:
                line += "*"
            else:
                line += " "
        rectangle.append(line)
    
    return rectangle

if __name__ == '__main__':
    WIDTH = 6
    HEIGHT = 4
    pattern = generate_hollow_rectangle(WIDTH, HEIGHT)
    for row in pattern:
        print(row)