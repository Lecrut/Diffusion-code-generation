def calculate_triangle_area(base, height):
    if not isinstance(base, (float, int)) or not isinstance(height, (float, int)):
        raise TypeError("Both base and height must be numbers.")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        sample_base = 7.5
        sample_height = 4.2
        area = calculate_triangle_area(sample_base, sample_height)
        print(area)
    except Exception as e:
        print(e)