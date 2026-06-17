import math
def convert_to_kilograms(mass: float, source_unit: str) -> float:
    conversion_factors = {
        'kg': 1.0,
        'g': 1e-3,
        'mg': 1e-6,
        't': 1e3,
        'lb': 453.59237,
        'oz': 28.349523125,
    }
    if source_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {source_unit}")
    return mass * conversion_factors[source_unit]
if __name__ == '__main__':
    test_cases = [
        (100.0, 'g'),
        (500.0, 'mg'),
        (2.5, 't'),
        (10.0, 'lb'),
        (32.0, 'oz')
    ]
    for mass_val, unit in test_cases:
        result = convert_to_kilograms(mass_val, unit)
        print(f"{mass_val} {unit} -> {result:.6f} kg")