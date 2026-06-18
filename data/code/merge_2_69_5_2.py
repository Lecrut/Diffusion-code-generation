from typing import Union
def convert_mass_to_si(mass_value: float, source_unit: str) -> float:
    conversion_factors = {
        'g': 1e-3,
        'mg': 1e-6,
        'ug': 1e-9,
        'lb': 0.45359237,
        'oz': 0.028349523125,
    }
    if source_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit '{source_unit}'. Supported units are {list(conversion_factors.keys())}.")
    return mass_value * conversion_factors[source_unit]
if __name__ == '__main__':
    test_cases = [
        (50, 'g'),
        (1000, 'mg'),
        (2.2, 'lb'),
        (483769.0, 'oz'),
    ]
    for value, unit in test_cases:
        result_kg = convert_mass_to_si(value, unit)
        print(f"{value} {unit} = {result_kg:.15f} kg")