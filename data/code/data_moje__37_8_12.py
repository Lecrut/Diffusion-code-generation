def validate_positive(value):
    if value <= 0:
        raise ValueError("Dimensions must be positive numbers.")

def calculate_parallelogram_area(base, height):
    validate_positive(base)
    validate_positive(height)
    return base * height

if __name__ == '__main__':
    base_value = 7
    height_value = 4
    area_result = calculate_parallelogram_area(base_value, height_value)
    print(area_result)