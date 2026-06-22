def calculate_triangle_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative values.")
    return 0.5 * base * height

if __name__ == '__main__':
    base_value = 10
    height_value = 5
    try:
        area = calculate_triangle_area(base_value, height_value)
        print(area)
    except ValueError as e:
        print(str(e))