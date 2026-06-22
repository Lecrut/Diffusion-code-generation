def validate_base_height(base, height):
    if base <= 0:
        raise ValueError("Base must be greater than zero.")
    if height <= 0:
        raise ValueError("Height must be greater than zero.")

def calculate_triangle_area(base, height):
    validate_base_height(base, height)
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        base = 8.0
        height = 6.0
        area = calculate_triangle_area(base, height)
        print(f"Triangle Area: {area}")
    except ValueError as e:
        print(e)