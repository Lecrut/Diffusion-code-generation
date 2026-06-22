def calculate_triangle_area(base, height):
    if base <= 0:
        raise ValueError("Base must be positive")
    if height <= 0:
        raise ValueError("Height must be positive")
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        base_value = 10
        height_value = 5
        area_result = calculate_triangle_area(base_value, height_value)
        print(area_result)
    except ValueError as e:
        print(e)