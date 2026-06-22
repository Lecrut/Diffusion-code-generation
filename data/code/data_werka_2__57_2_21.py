def calculate_triangle_area(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Base and height must be numbers")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive values")
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        base = 10.0
        height = 5.0
        area = calculate_triangle_area(base, height)
        print(f"The area of the triangle with base {base} and height {height} is: {area}")
    except (TypeError, ValueError) as e:
        print(e)