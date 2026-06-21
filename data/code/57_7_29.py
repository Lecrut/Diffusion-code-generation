def validate_dimensions(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Base and height must be numbers")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers")

def calculate_area(base, height):
    validate_dimensions(base, height)
    return 0.5 * base * height

if __name__ == '__main__':
    base = 9
    height = 3
    area = calculate_area(base, height)
    print(area)