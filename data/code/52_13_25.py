def calculate_area_of_triangle(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

def validate_inputs(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Base and height must be numbers.")

if __name__ == '__main__':
    base = 18
    height = 6
    validate_inputs(base, height)
    area = calculate_area_of_triangle(base, height)
    print(area)