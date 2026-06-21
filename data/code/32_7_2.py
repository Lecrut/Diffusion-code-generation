def calculate_rectangle_area(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Width and height must be numbers")
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative")
    return width * height

if __name__ == '__main__':
    integer_width = 5
    integer_height = 10
    float_width = 3.5
    float_height = 4.2
    print(calculate_rectangle_area(integer_width, integer_height))
    print(calculate_rectangle_area(float_width, float_height))