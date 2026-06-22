def validate_input(base, height):
    if not isinstance(base, (int, float)):
        raise ValueError("Base must be a number")
    if not isinstance(height, (int, float)):
        raise ValueError("Height must be a number")
    if base <= 0:
        raise ValueError("Base must be positive")
    if height <= 0:
        raise ValueError("Height must be positive")

def calculate_triangle_area(base, height):
    validate_input(base, height)
    return 0.5 * base * height

if __name__ == '__main__':
    base = 8.0
    height = 3.0
    area = calculate_triangle_area(base, height)
    print(f"Area of triangle with base {base} and height {height}: {area}")