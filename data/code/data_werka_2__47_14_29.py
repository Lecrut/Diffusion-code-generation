def validate_positive_number(value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{value} must be a number.")
    if value <= 0:
        raise ValueError(f"{value} must be a positive number.")

def calculate_triangle_area(base, height):
    validate_positive_number(base)
    validate_positive_number(height)
    return 0.5 * base * height

if __name__ == '__main__':
    sample_base = 12
    sample_height = 7
    try:
        area = calculate_triangle_area(sample_base, sample_height)
        print(f"The area of the triangle with base {sample_base} and height {sample_height} is: {area}")
    except (TypeError, ValueError) as e:
        print(e)