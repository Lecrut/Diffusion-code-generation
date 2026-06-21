def calculate_rectangle_area(width, height):
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative")
    return width * height

if __name__ == '__main__':
    w = 5
    h = 10
    area = calculate_rectangle_area(w, h)
    print(area)