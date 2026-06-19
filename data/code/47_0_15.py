def validate_input(base, height):
    if not isinstance(base, (float, int)) or not isinstance(height, (float, int)):
        raise TypeError("Both base and height must be numbers.")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")

def calculate_triangle_area(base, height):
    validate_input(base, height)
    area = 0.5 * base * height
    return area

if __name__ == '__main__':
    base_value = 12.5
    height_value = 4.0
    try:
        result = calculate_triangle_area(base_value, height_value)
        print(result)
    except Exception as e:
        print(e)