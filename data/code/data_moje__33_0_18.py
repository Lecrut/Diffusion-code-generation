def calculate_triangle_area(base, height):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a numeric value.")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a numeric value.")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive values.")
    return 0.5 * base * height

if __name__ == '__main__':
    result = calculate_triangle_area(10, 5)
    print(result)