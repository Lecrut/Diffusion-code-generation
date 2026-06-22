def calculate_rectangle_area(width, height):
    if not isinstance(width, (int, float)):
        raise TypeError("Width must be a numeric type")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a numeric type")
    return width * height

if __name__ == '__main__':
    width = 10
    height = 5
    area = calculate_rectangle_area(width, height)
    print(area)