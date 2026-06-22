def calculate_triangle_area(base, height):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number")
    if base < 0:
        raise ValueError("Base must be non-negative")
    if height < 0:
        raise ValueError("Height must be non-negative")
    return 0.5 * base * height

if __name__ == '__main__':
    base_value = 10
    height_value = 5
    area = calculate_triangle_area(base_value, height_value)
    print(area)