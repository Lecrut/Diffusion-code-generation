def calculate_triangle_area(base: float, height: float) -> float:
    if base < 0 or height < 0:
        raise ValueError('Base and height must be non-negative.')
    return 0.5 * base * height
if __name__ == '__main__':
    sample_base = 10.0
    sample_height = 5.0
    area = calculate_triangle_area(sample_base, sample_height)
    print(area)