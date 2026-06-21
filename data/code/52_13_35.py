def calculate_triangle_area(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Base and height must be numbers.")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    test_base = 25
    test_height = 12
    try:
        area = calculate_triangle_area(test_base, test_height)
        print(f"The area of the triangle with base {test_base} and height {test_height} is: {area}")
    except ValueError as e:
        print(e)