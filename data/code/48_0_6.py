def validate_dimensions(base, height):
    if base <= 0 or height <= 0:
        return False
    return True

def calculate_area(base, height):
    if not validate_dimensions(base, height):
        raise ValueError("Invalid dimensions: Base and height must be positive numbers.")
    return base * height

if __name__ == '__main__':
    base = 6
    height = 8
    area = calculate_area(base, height)
    print(area)