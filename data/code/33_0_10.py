def calculate_triangle_area(base, height):
    if not isinstance(base, (int, float)):
        raise TypeError("base must be a numeric value")
    if not isinstance(height, (int, float)):
        raise TypeError("height must be a numeric value")
    if base < 0 or height < 0:
        raise ValueError("base and height must be non-negative values")
    return 0.5 * base * height

if __name__ == '__main__':
    base_value = 10
    height_value = 5
    result = calculate_triangle_area(base_value, height_value)
    print(result)