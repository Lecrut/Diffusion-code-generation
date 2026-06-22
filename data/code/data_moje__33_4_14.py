def calculate_triangle_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative")
    return 0.5 * base * height

if __name__ == '__main__':
    sample_base = 10.0
    sample_height = 5.0
    try:
        area = calculate_triangle_area(sample_base, sample_height)
        print(area)
    except ValueError as e:
        print(str(e))

    negative_base = -3.0
    negative_height = 4.0
    try:
        invalid_area = calculate_triangle_area(negative_base, negative_height)
        print(invalid_area)
    except ValueError as e:
        print(str(e))

    zero_base = 0.0
    positive_height = 7.0
    try:
        zero_area = calculate_triangle_area(zero_base, positive_height)
        print(zero_area)
    except ValueError as e:
        print(str(e))