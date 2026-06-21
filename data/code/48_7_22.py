def validate_dimensions(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Base and height must be numbers.")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")

def calculate_area(base, height):
    validate_dimensions(base, height)
    return base * height

if __name__ == '__main__':
    base = 6.3
    height = 2.9
    area = calculate_area(base, height)
    print(area)