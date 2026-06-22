def validate_input(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a number.")
    if value <= 0:
        raise ValueError("Input must be a positive number.")

def calculate_triangle_area(base, height):
    validate_input(base)
    validate_input(height)
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        base = 15
        height = 6
        area = calculate_triangle_area(base, height)
        print(f"The area of the triangle is: {area}")
    except (TypeError, ValueError) as e:
        print(e)