import sys
def convert_to_kg(value: float, unit: str) -> float:
    conversions = {
        'kg': 1.0,
        'tonne': 1000.0,
        'mg': 0.000001,
        'g': 0.001,
        'lb': 0.45359237,
        'oz': 0.028349523125,
    }
    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
    return value * conversions[unit]
if __name__ == '__main__':
    test_cases = [
        (1.0, 'lb'),
        (1000.0, 'g'),
        (500000.0, 'mg'),
        (2.0, 'tonne'),
        (32.17406875, 'oz'),
    ]
    for mass_val, unit in test_cases:
        result = convert_to_kg(mass_val, unit)
        print(f"{mass_val} {unit} -> {result:.9f} kg")