def calculate_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        sample_base = 18.0
        sample_height = 6.0
        result_area = calculate_triangle_area(sample_base, sample_height)
        print(result_area)
    except ValueError as e:
        print(e)