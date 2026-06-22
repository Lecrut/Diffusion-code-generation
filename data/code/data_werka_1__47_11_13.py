def validate_dimensions(base, height):
    if base <= 0:
        raise ValueError("Base must be a positive number.")
    if height <= 0:
        raise ValueError("Height must be a positive number.")

def calculate_triangle_area(base, height):
    validate_dimensions(base, height)
    return 0.5 * base * height

if __name__ == '__main__':
    base_val = 20.0
    height_val = 10.0
    try:
        area = calculate_triangle_area(base_val, height_val)
        print(area)
    except ValueError as e:
        print(e)