def validate_input(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Base and height must be numbers.")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")

def calculate_triangle_area(base, height):
    validate_input(base, height)
    return 0.5 * base * height

if __name__ == '__main__':
    base_val = 20.0
    height_val = 10.0
    area = calculate_triangle_area(base_val, height_val)
    print(area)