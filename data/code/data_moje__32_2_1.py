def calculate_rectangle_area(width: float, height: float) -> float:
    return width * height

if __name__ == '__main__':
    width = 5
    height = 10
    area = calculate_rectangle_area(width, height)
    print(area)