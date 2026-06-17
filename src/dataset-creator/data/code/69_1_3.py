import math
def convert_to_kilograms(mass_value: float, source_unit: str) -> float:
    conversion_factors = {
        'kg': 1.0,
        'g': 1e-3,
        'mg': 1e-6,
        't': 1e3,
        'lb': 453.59237,
        'oz': 0.028349523125,
    }
    if source_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {source_unit}")
    return mass_value * conversion_factors[source_unit]
if __name__ == '__main__':
    test_cases = [
        (10.5, 'g'),
        (2.3e6, 'mg'),
        (5.0, 't'),
        (100.0, 'lb')
    ]
    for mass_val, unit in test_cases:
        result = convert_to_kilograms(mass_val, unit)
        print(f"{mass_val} {unit} -> {result:.6f} kg")