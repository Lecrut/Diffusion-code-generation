import sys
def convert_to_kilograms(mass_value: float, source_unit: str) -> float:
    conversion_factors = {
        'kg': 1.0,
        'g': 1e-3,
        'mg': 1e-6,
        't': 1e3,
        'lb': 453.59237,
        'oz': 28.349523125,
    }
    if source_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit '{source_unit}'. Supported units are {list(conversion_factors.keys())}.")
    factor = conversion_factors[source_unit]
    from decimal import Decimal, getcontext
    getcontext().prec = 28
    mass_decimal = Decimal(str(mass_value)) * Decimal(str(factor))
    return float(mass_decimal)
if __name__ == '__main__':
    test_cases = [
        ('5', 'g'),
        (100, 'mg'),
        (0.5, 'lb'),
        (2, 'oz'),
        (1e9, 't')
    ]
    for mass_str, unit in test_cases:
        result = convert_to_kilograms(float(mass_str), unit)
        print(f"{mass_str} {unit} -> {result:.6f} kg")