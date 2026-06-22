def calculate_rectangle_area(width: float, height: float) -> float:
    if width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive numbers.")
    return width * height

if __name__ == '__main__':
    width = 10
    height = 5
    area = calculate_rectangle_area(width, height)
    print(area)