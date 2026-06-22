def compute_area_parallelogram(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Base and height must be numeric types.")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive.")
    area = base * height
    return float(area)

if __name__ == '__main__':
    BASE_VALUE = 12.5
    HEIGHT_VALUE = 8.0
    calculated_area = compute_area_parallelogram(BASE_VALUE, HEIGHT_VALUE)
    print(calculated_area)