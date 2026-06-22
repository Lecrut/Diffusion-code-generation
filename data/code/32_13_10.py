def calculate_area(width, height):
    if width <= 0 or height <= 0:
        return 0
    return width * height

if __name__ == '__main__':
    w = 7
    h = 3
    area = calculate_area(w, h)
    print(area)