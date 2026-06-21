def calculate_triangle_area(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Base and height must be numbers.")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        sample_base = 12
        sample_height = 6
        area = calculate_triangle_area(sample_base, sample_height)
        print(f"The area of the triangle is: {area}")
    except (TypeError, ValueError) as e:
        print(e)