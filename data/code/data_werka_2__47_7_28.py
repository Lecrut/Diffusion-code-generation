def calculate_triangle_area(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Base and height must be numbers.")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    base_value = 15
    height_value = 8
    area_result = calculate_triangle_area(base_value, height_value)
    print(area_result)