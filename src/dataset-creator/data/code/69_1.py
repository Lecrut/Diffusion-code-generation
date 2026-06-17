import sys
def convert_to_kg(mass: float, source_unit: str) -> float:
    conversion_factors = {
        'kg': 1.0,
        'lb': 0.45359237,
        'oz': 0.028349523125,
        'g': 0.001,
        'tonne': 1000.0,
    }
    if source_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {source_unit}")
    return mass * conversion_factors[source_unit]
if __name__ == '__main__':
    test_cases = [
        (5.0, 'lb'),
        (16.0, 'oz'),
        (2.5, 'g'),
        (1.0, 'tonne'),
        (70.0, 'kg')
    ]
    for mass_val, unit in test_cases:
        result = convert_to_kg(mass_val, unit)
        print(f"{mass_val} {unit} -> {result:.6f} kg")