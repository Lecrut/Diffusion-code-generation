def calculate_triangle_area(base, height):
    if base <= 0:
        raise ValueError("Base must be positive")
    if height <= 0:
        raise ValueError("Height must be positive")
    return 0.5 * base * height

if __name__ == '__main__':
    base_val = 8
    height_val = 6
    area_result = calculate_triangle_area(base_val, height_val)
    print(area_result)