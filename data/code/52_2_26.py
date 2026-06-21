def validate_positive_number(value, name):
    if value <= 0:
        raise ValueError(f"The {name} must be a positive number.")

def calculate_triangle_area(base, height):
    validate_positive_number(base, 'base')
    validate_positive_number(height, 'height')
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        area = calculate_triangle_area(9, 4)
        print(area)
    except ValueError as e:
        print(e)