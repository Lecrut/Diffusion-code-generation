def _validate_dimension(value, name):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be int or float")
    if value <= 0:
        raise ValueError(f"{name} must be positive")

def get_parallelogram_area(base, height):
    _validate_dimension(base, "base")
    _validate_dimension(height, "height")
    return base * height

if __name__ == '__main__':
    sample_base = 8.5
    sample_height = 6.2
    area_result = get_parallelogram_area(sample_base, sample_height)
    print(area_result)