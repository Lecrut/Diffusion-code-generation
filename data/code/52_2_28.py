def validate_positive_number(value):
    if value <= 0:
        raise ValueError("The provided value must be a positive number.")

def calculate_triangle_area(base, height):
    validate_positive_number(base)
    validate_positive_number(height)
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        sample_base = 9
        sample_height = 4
        area = calculate_triangle_area(sample_base, sample_height)
        print(area)
    except ValueError as e:
        print(e)

    try:
        invalid_base = -5
        invalid_height = 3
        area = calculate_triangle_area(invalid_base, invalid_height)
        print(area)
    except ValueError as e:
        print(e)