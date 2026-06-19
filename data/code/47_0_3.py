def calculate_triangle_area(base, height):
    try:
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        return 0.5 * base * height
    except TypeError:
        raise TypeError("Both base and height must be floating-point numbers.")

if __name__ == '__main__':
    sample_base = 10.0
    sample_height = 5.0
    area = calculate_triangle_area(sample_base, sample_height)
    print(area)