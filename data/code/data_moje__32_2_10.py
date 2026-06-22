def calculate_rectangle_area(width: float, height: float) -> float:
    return width * height

if __name__ == '__main__':
    width = 10.5
    height = 4.2
    area = calculate_rectangle_area(width, height)
    print(area)