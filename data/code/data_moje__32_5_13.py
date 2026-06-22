def calculate_rectangle_area(width, height):
    if not isinstance(width, (int, float)):
        raise TypeError("Width must be a numeric value")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a numeric value")
    return width * height

if __name__ == '__main__':
    width = 5
    height = 10
    result = calculate_rectangle_area(width, height)
    print(result)