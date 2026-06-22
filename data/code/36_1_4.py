def trapezoid_area(base1, base2, height):
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError('Base lengths and height must be non-negative.')
    return 0.5 * (base1 + base2) * height
if __name__ == '__main__':
    sample_base1 = 5.0
    sample_base2 = 7.0
    sample_height = 4.0
    area = trapezoid_area(sample_base1, sample_base2, sample_height)
    print(area)