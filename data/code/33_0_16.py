def calculate_triangle_area(base, height):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a numeric value")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a numeric value")
    if base < 0:
        raise ValueError("Base must be non-negative")
    if height < 0:
        raise ValueError("Height must be non-negative")
    return 0.5 * base * height

if __name__ == '__main__':
    base = 10
    height = 5
    area = calculate_triangle_area(base, height)
    print(area)