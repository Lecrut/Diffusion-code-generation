def validate_dimensions(base: float, height: float) -> tuple[float, float]:
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a numeric type.")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a numeric type.")
    if base <= 0:
        raise ValueError("Base must be positive.")
    if height <= 0:
        raise ValueError("Height must be positive.")
    return base, height

def compute_parallelogram_area(base: float, height: float) -> float:
    valid_base, valid_height = validate_dimensions(base, height)
    return valid_base * valid_height

if __name__ == '__main__':
    base_value = 12
    height_value = 8
    result = compute_parallelogram_area(base_value, height_value)
    print(result)