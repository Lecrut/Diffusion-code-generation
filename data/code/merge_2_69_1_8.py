import sys
def convert_mass(mass_value: float, source_unit: str) -> float:
    conversion_factors = {
        'kg': 1.0,
        'g': 1e-3,
        'mg': 1e-6,
        'lb': 453.59237e-3,
        'oz': 28.349523125e-3,
    }
    if source_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {source_unit}")
    return mass_value * conversion_factors[source_unit]
if __name__ == '__main__':
    test_cases = [
        (10.0, 'g'),
        (5000.0, 'mg'),
        (2.0, 'lb'),
        (64.0, 'oz'),
        (7.5, 'kg')
    ]
    for mass_val, unit in test_cases:
        result = convert_mass(mass_val, unit)
        print(f"{mass_val} {unit} -> {result:.12f} kg")