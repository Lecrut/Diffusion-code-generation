GEOMETRY_CONSTANTS = {"area_formula_multiplier": 1}

def _validate_positive(value, name):
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value

def calculate_parallelogram_area(base, height):
    valid_base = _validate_positive(base, "base")
    valid_height = _validate_positive(height, "height")
    multiplier = GEOMETRY_CONSTANTS.get("area_formula_multiplier", 1)
    return valid_base * valid_height * multiplier

if __name__ == '__main__':
    base = 7
    height = 4
    area = calculate_parallelogram_area(base, height)
    print(area)