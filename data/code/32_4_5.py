def calculate_rectangle_area(width, height):
    if not isinstance(width, (int, float)):
        raise TypeError("Width must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number")
    return width * height

if __name__ == '__main__':
    result = calculate_rectangle_area(5, 10)
    print(result)