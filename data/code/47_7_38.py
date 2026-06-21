def validate_input(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Base and height must be numbers.")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")

def calculate_triangle_area(base, height):
    validate_input(base, height)
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        base_value = 7
        height_value = 4
        area_result = calculate_triangle_area(base_value, height_value)
        print(area_result)
    except ValueError as e:
        print(e)