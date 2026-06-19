def validate_input(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number.")
    return value

def calculate_area(base, height):
    base = validate_input(base)
    height = validate_input(height)
    area = 0.5 * base * height
    return area

if __name__ == '__main__':
    sample_base = 7.5
    sample_height = 4.0
    result = calculate_area(sample_base, sample_height)
    print(result)