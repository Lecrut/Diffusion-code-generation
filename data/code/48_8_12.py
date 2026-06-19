def calculate_area(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Both base and height must be numbers.")
    if base <= 0 or height <= 0:
        raise ValueError("Both base and height must be positive numbers.")
    return base * height

if __name__ == '__main__':
    try:
        rectangle_base = 8.5
        rectangle_height = 6.3
        area_result = calculate_area(rectangle_base, rectangle_height)
        print(area_result)
    except ValueError as e:
        print(e)