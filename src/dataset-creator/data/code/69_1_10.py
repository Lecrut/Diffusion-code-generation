import sys
def convert_to_kg(mass_value: float, source_unit: str) -> float:
    conversion_factors = {
        'kg': 1.0,
        'gram': 1e-3,
        'milligram': 1e-6,
        'microgram': 1e-9,
        'tonne': 1e3,
        'pound': 453.59237,
        'ounce': 0.028349523125,
    }
    if source_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {source_unit}")
    return mass_value * conversion_factors[source_unit]
if __name__ == '__main__':
    test_cases = [
        (10.5, 'gram'),
        (2.34e-6, 'microgram'),
        (5000, 'tonne'),
        (7.89, 'pound'),
        (100, 'ounce')
    ]
    for mass_val, unit in test_cases:
        result = convert_to_kg(mass_val, unit)
        print(f"{mass_val} {unit} -> {result:.6f} kg")