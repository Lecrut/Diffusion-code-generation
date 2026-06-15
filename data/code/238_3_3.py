def draw_box(width, height):
    for y in range(height):
        line = ""
        for x in range(width):
            if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                line += "#"
            else:
                line += " "
        print(line)
if __name__ == '__main__':
    box_width = 10
    box_height = 5
    draw_box(box_width, box_height)