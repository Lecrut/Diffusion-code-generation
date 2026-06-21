def validate_positive_number(value, name):
    if value <= 0:
        raise ValueError(f"{name} must be a positive number.")

def calculate_triangle_area(base, height):
    validate_positive_number(base, "Base")
    validate_positive_number(height, "Height")
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        sample_base = 9
        sample_height = 4
        area = calculate_triangle_area(sample_base, sample_height)
        print(area)
    except ValueError as e:
        print(e)