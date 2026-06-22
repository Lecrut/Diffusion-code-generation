def calculate_triangle_area(base, height):
    if base <= 0:
        raise ValueError("Base must be a positive number.")
    if height <= 0:
        raise ValueError("Height must be a positive number.")
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        base_value = 9
        height_value = 4
        area = calculate_triangle_area(base_value, height_value)
        print(area)
    except ValueError as e:
        print(e)