def convert_volume(value: float, unit: str) -> float:
    conversion_factors = {'liters': 1.0, 'l': 1.0, 'milliliters': 0.001, 'ml': 0.001, 'microliters': 1e-06, 'ul': 1e-06, 'gallons': 3.785411784, 'gal': 3.785411784, 'cubic_meters': 1000.0, 'm3': 1000.0, 'cubic_feet': 28.316846592, 'ft3': 28.316846592, 'cubic_inches': 0.016387064, 'in3': 0.016387064, 'cubic_centimeters': 0.001, 'cm3': 0.001, 'cubic_millimeters': 1e-06, 'mm3': 1e-06, 'pints': 0.473176473, 'pt': 0.473176473, 'quarts': 0.946352946, 'qt': 0.946352946, 'fluid_ounces': 0.0295735295625, 'floz': 0.0295735295625}
    unit_lower = unit.lower().strip()
    if unit_lower not in conversion_factors:
        raise ValueError(f'Unsupported unit: {unit}')
    return value * conversion_factors[unit_lower]
if __name__ == '__main__':
    print(convert_volume(1, 'gallons'))
    print(convert_volume(500, 'milliliters'))
    print(convert_volume(1, 'cubic_meters'))
    print(convert_volume(10.5, 'cubic_feet'))