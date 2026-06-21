def validate_input(value, name):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number.")
    if value <= 0:
        raise ValueError(f"{name} must be a positive number.")

def calculate_area(base, height):
    validate_input(base, 'base')
    validate_input(height, 'height')
    area = base * height
    return area

if __name__ == '__main__':
    sample_base = 9.1
    sample_height = 6.4
    try:
        result = calculate_area(sample_base, sample_height)
        print(result)
    except Exception as e:
        print(e)