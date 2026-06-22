def calculate_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    sample_base = 10
    sample_height = 5
    result = calculate_triangle_area(sample_base, sample_height)
    print(result)