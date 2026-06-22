BASE_AREA = 25.0
HEIGHT = 7.5

def _validate_positive(value, name):
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return True

def calculate_prism_volume(base_area, height):
    _validate_positive(base_area, "base_area")
    _validate_positive(height, "height")
    return base_area * height

if __name__ == '__main__':
    result = calculate_prism_volume(BASE_AREA, HEIGHT)
    print(result)