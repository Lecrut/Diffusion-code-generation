def _validate_dimensions(base, height):
    if not (isinstance(base, (int, float)) and isinstance(height, (int, float))):
        raise TypeError("Base and height must be numeric.")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive.")

def calculate_parallelogram_area(base, height):
    _validate_dimensions(base, height)
    return base * height

if __name__ == '__main__':
    sample_base = 8.5
    sample_height = 4.2
    computed_area = calculate_parallelogram_area(sample_base, sample_height)
    print(computed_area)