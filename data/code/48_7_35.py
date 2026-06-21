def validate_positive(number, name):
    if number <= 0:
        raise ValueError(f"{name} must be a positive number.")

def calculate_area(base, height):
    validate_positive(base, "base")
    validate_positive(height, "height")
    return base * height

if __name__ == '__main__':
    sample_base = 8.4
    sample_height = 5.1
    calculated_area = calculate_area(sample_base, sample_height)
    print(calculated_area)