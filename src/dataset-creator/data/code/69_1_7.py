import sys
def convert_to_kg(mass: float, unit: str) -> float:
    conversion_factors = {
        'kg': 1.0,
        'lb': 0.45359237,
        'oz': 0.028349523125,
        'g': 0.001,
    }
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit '{unit}'. Supported units are {list(conversion_factors.keys())}")
    return mass * conversion_factors[unit]
if __name__ == '__main__':
    test_cases = [
        (10.5, 'lb'),
        (200, 'oz'),
        (5, 'g'),
        (3, 'kg')
    ]
    for mass_val, unit in test_cases:
        result_kg = convert_to_kg(mass_val, unit)
        print(f"{mass_val} {unit} = {result_kg:.10f} kg")