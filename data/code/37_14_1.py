def compute_parallelogram_area(base, height):
    if base < 0 or height < 0:
        raise ValueError('Base and height must be non-negative values.')
    return base * height
if __name__ == '__main__':
    base = 10.5
    height = 7.2
    area = compute_parallelogram_area(base, height)
    print(area)