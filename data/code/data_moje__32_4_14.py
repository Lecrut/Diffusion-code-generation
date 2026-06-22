def calculate_rectangle_area(width, height):
    if not isinstance(width, (int, float)):
        raise TypeError("width must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("height must be a number")
    if isinstance(width, bool):
        raise TypeError("width must not be bool")
    if isinstance(height, bool):
        raise TypeError("height must not be bool")
    return width * height

if __name__ == '__main__':
    result = calculate_rectangle_area(5, 10)
    print(result)