def validate_input(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Base and height must be numbers.")
    if value <= 0:
        raise ValueError("Base and height must be positive numbers.")

def calculate_triangle_area(base, height):
    validate_input(base)
    validate_input(height)
    return 0.5 * base * height

if __name__ == '__main__':
    base_value = 7
    height_value = 4
    area_result = calculate_triangle_area(base_value, height_value)
    print(area_result)