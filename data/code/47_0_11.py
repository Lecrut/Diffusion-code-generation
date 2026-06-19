def validate_input(base, height):
    if not isinstance(base, float) or not isinstance(height, float):
        raise TypeError("Both base and height must be floating-point numbers.")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")

def calculate_triangle_area(base, height):
    validate_input(base, height)
    return 0.5 * base * height

if __name__ == '__main__':
    sample_base = 7.0
    sample_height = 4.0
    try:
        area = calculate_triangle_area(sample_base, sample_height)
        print(area)
    except Exception as e:
        print(e)