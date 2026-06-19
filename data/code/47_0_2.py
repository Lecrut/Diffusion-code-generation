def calculate_triangle_area(base, height):
    try:
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        area = 0.5 * base * height
        return area
    except TypeError:
        raise TypeError("Both base and height must be floating-point numbers.")

if __name__ == '__main__':
    sample_base = 10.0
    sample_height = 5.0
    try:
        result = calculate_triangle_area(sample_base, sample_height)
        print(result)
    except Exception as e:
        print(e)