def compute_trapezoid_area(base1, base2, height):
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    sample_base1 = 10.0
    sample_base2 = 5.0
    sample_height = 7.0
    area = compute_trapezoid_area(sample_base1, sample_base2, sample_height)
    print(area)