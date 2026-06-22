def calculate_rectangle_area(width: float, height: float) -> float:
    return width * height

if __name__ == '__main__':
    w = 5.0
    h = 3.0
    area = calculate_rectangle_area(w, h)
    print(area)