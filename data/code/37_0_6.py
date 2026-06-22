def _validate_dimensions(base, height):
    if base <= 0 or height <= 0:
        return 0.0
    return 1.0

def calculate_parallelogram_area(base, height):
    factor = _validate_dimensions(base, height)
    return base * height * factor

if __name__ == '__main__':
    b = 7.5
    h = 4.2
    area = calculate_parallelogram_area(b, h)
    print(area)