import sys
def convert_mass_to_kg(mass_value: float, source_unit: str) -> float:
    conversion_factors = {
        'kg': 1.0,
        'gram': 1e-3,
        'milligram': 1e-6,
        'microgram': 1e-9,
        'pound': 453.59237,
        'ounce': 0.028349523125,
    }
    if source_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {source_unit}")
    return mass_value * conversion_factors[source_unit]
if __name__ == '__main__':
    test_cases = [
        (10.0, 'gram'),
        (5000.0, 'milligram'),
        (2.0, 'pound'),
        (32.0, 'ounce')
    ]
    for mass, unit in test_cases:
        result = convert_mass_to_kg(mass, unit)
        print(f"{mass} {unit} -> {result:.15f} kg")