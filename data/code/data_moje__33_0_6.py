def calculate_triangle_area(base, height):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a numeric type.")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a numeric type.")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    sample_base = 10
    sample_height = 5
    area = calculate_triangle_area(sample_base, sample_height)
    print(area)