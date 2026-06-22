def calculate_triangle_area(base, height):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive")
    return 0.5 * base * height

if __name__ == '__main__':
    base_val = 10
    height_val = 5
    result = calculate_triangle_area(base_val, height_val)
    print(result)