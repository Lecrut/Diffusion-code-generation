def convert_distance(distance: float, target_unit: str, base_unit: str = 'meters') -> float:
    if distance != distance:
        raise ValueError("Distance cannot be NaN")
    conversions = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.344,
        'yards': 0.9144,
        'feet': 0.3048,
        'inches': 0.0254
    }
    if base_unit not in conversions or target_unit not in conversions:
        raise ValueError(f"Unknown unit: {base_unit} or {target_unit}")
    try:
        value_in_base = distance * conversions[base_unit]
        result = value_in_base / conversions[target_unit]
        return result
    except ZeroDivisionError:
        raise ArithmeticError("Division by zero occurred during conversion")

if __name__ == '__main__':
    sample_distance = 100.0
    sample_target = 'feet'
    result = convert_distance(sample_distance, sample_target)
    print(result)