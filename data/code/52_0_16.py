def validate_input(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Base and height must be numbers.")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive.")

def calculate_area(base, height):
    validate_input(base, height)
    area = 0.5 * base * height
    return area

if __name__ == '__main__':
    base_sample = 7.5
    height_sample = 4.2
    result = calculate_area(base_sample, height_sample)
    print(result)