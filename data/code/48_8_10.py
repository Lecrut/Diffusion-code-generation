def validate_input(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be an integer or a float.")
    if value <= 0:
        raise ValueError("Input must be greater than zero.")

def calculate_area(base, height):
    validate_input(base)
    validate_input(height)
    return base * height

if __name__ == '__main__':
    sample_base = 6.3
    sample_height = 4.7
    area = calculate_area(sample_base, sample_height)
    print(area)