def validate_positive_number(value):
    if value <= 0:
        raise ValueError("The value must be a positive number.")

def calculate_triangle_area(base, height):
    validate_positive_number(base)
    validate_positive_number(height)
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        area = calculate_triangle_area(7, 3)
        print(area)
    except ValueError as e:
        print(e)