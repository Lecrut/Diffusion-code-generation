def draw_box(width, height):
    if width <= 0 or height <= 0:
        return "Invalid dimensions"
    border = "*"
    top_bottom = border * width
    side = border * (height - 2)
    top_line = border + " " * (width - 2) + border
    middle_line = border + " " * (width - 2) + border
    bottom_line = border + " " * (width - 2) + border
    box = [top_line, side, middle_line, side, bottom_line]
    return "\n".join(box)
if __name__ == '__main__':
    box_width = 10
    box_height = 5
    print(draw_box(box_width, box_height))