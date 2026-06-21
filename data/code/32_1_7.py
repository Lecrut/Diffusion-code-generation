def calculate_rectangle_area(width: float, height: float) -> float:
    return float(width * height)

if __name__ == '__main__':
    width = 5.5
    height = 3.2
    area = calculate_rectangle_area(width, height)
    print(area)