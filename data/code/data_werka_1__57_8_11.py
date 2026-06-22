def validate_base_height(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Base and height must be numbers")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive")

def calculate_area(base, height):
    validate_base_height(base, height)
    return 0.5 * base * height

if __name__ == '__main__':
    sample_base = 10
    sample_height = 5
    area = calculate_area(sample_base, sample_height)
    print(area)