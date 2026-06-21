def calculate_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError('Base and height must be positive numbers.')
    area = 0.5 * base * height
    return area
if __name__ == '__main__':
    sample_base = 7
    sample_height = 4
    calculated_area = calculate_triangle_area(sample_base, sample_height)
    print(calculated_area)