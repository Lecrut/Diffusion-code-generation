def validate_positive_number(value, name):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number.")
    if value <= 0:
        raise ValueError(f"{name} must be a positive number.")

def calculate_area(base, height):
    validate_positive_number(base, "base")
    validate_positive_number(height, "height")
    return base * height

if __name__ == '__main__':
    sample_base = 9.1
    sample_height = 6.4
    area = calculate_area(sample_base, sample_height)
    print(area)