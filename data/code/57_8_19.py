def validate_dimensions(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers")

def calculate_area(base, height):
    validate_dimensions(base, height)
    return base * height

if __name__ == '__main__':
    base_sample = 10
    height_sample = 5
    area_result = calculate_area(base_sample, height_sample)
    print(area_result)