def calculate_rectangle_area(width, height):
    if width <= 0 or height <= 0:
        return 0
    return width * height

if __name__ == '__main__':
    w = 5
    h = 3.5
    area = calculate_rectangle_area(w, h)
    print(area)