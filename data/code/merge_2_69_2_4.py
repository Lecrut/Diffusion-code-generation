def get_mass_conversion_factors():
    return {
        'kg_to_g': 1000,
        'g_to_kg': 0.001,
        'lb_to_kg': 0.45359237,
        'kg_to_lb': 2.20462262,
    }
def convert_mass(value: float, from_unit: str, to_unit: str) -> float:
    factors = get_mass_conversion_factors()
    if from_unit == 'lb' and to_unit in ('g', 'kg'):
        value *= 0.45359237
    elif from_unit == 'g' and to_unit in ('lb', 'kg'):
        value /= 1000 * 0.45359237 if to_unit == 'lb' else value / 1000
    return round(value, 6)
if __name__ == '__main__':
    test_cases = [
        ('kg', 'g', 1),
        ('g', 'kg', 500),
        ('lb', 'kg', 2.2),
        ('kg', 'lb', 10),
    ]
    for start_unit, end_unit, value in test_cases:
        result = convert_mass(value, start_unit, end_unit)
        print(f"{value} {start_unit} to {end_unit}: {result}")