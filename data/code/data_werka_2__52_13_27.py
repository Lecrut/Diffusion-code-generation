def calculate_triangle_area(base, height):
    if not (isinstance(base, (int, float)) and isinstance(height, (int, float))):
        raise ValueError("Base and height must be numbers.")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    base = 25
    height = 12
    try:
        area = calculate_triangle_area(base, height)
        print(f"The area of the triangle is: {area}")
    except ValueError as e:
        print(e)