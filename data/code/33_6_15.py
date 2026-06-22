DIMENSION_UNITS = {
    "base": "length",
    "height": "length",
    "area": "square_units"
}

def _validate_positive(value: float, name: str) -> float:
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value

def calculate_triangle_area(base: float, height: float) -> float:
    validated_base = _validate_positive(base, "Base")
    validated_height = _validate_positive(height, "Height")
    return 0.5 * validated_base * validated_height

if __name__ == '__main__':
    test_base = 8.0
    test_height = 4.0
    result = calculate_triangle_area(test_base, test_height)
    print(result)