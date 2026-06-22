def calculate_rectangle_area(width, height):
    if not isinstance(width, (int, float)):
        raise TypeError("Width must be a number.")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number.")
    return width * height

if __name__ == '__main__':
    width_value = 5
    height_value = 10
    result = calculate_rectangle_area(width_value, height_value)
    print(result)