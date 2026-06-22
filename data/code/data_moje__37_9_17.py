def _validate_dimensions(base, height):
    if base <= 0:
        raise ValueError("Base must be positive")
    if height <= 0:
        raise ValueError("Height must be positive")

def calculate_parallelogram_area(base, height):
    _validate_dimensions(base, height)
    return base * height

if __name__ == '__main__':
    sample_base = 7.5
    sample_height = 4.2
    result = calculate_parallelogram_area(sample_base, sample_height)
    print(result)