def validate_input(base, height):
    if not isinstance(base, (float, int)) or not isinstance(height, (float, int)):
        raise TypeError("Both base and height must be numbers.")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")

def calculate_triangle_area(base, height):
    validate_input(base, height)
    area = 0.5 * base * height
    return area

if __name__ == '__main__':
    sample_base = 12.0
    sample_height = 7.0
    try:
        result = calculate_triangle_area(sample_base, sample_height)
        print(result)
    except Exception as e:
        print(e)