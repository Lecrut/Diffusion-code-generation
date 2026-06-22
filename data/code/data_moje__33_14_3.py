def calculate_triangle_area(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Base and height must be numeric types.")
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative.")
    return 0.5 * base * height

if __name__ == '__main__':
    sample_base = 10
    sample_height = 5
    area = calculate_triangle_area(sample_base, sample_height)
    print(area)

    sample_base_2 = 7.5
    sample_height_2 = 4.0
    area_2 = calculate_triangle_area(sample_base_2, sample_height_2)
    print(area_2)

    try:
        calculate_triangle_area("invalid", 5)
    except TypeError as e:
        print(e)

    try:
        calculate_triangle_area(-3, 5)
    except ValueError as e:
        print(e)