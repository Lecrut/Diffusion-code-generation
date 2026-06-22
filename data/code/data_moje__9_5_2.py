def convert_volume_to_liters(value: float, unit: str) -> float:
    unit_lower = unit.lower().strip()
    factors = {'l': 1.0, 'liter': 1.0, 'liters': 1.0, 'ml': 0.001, 'milliliter': 0.001, 'milliliters': 0.001, 'm3': 1000.0, 'cubic meter': 1000.0, 'cm3': 0.001, 'cubic centimeter': 0.001, 'mm3': 1e-06, 'cubic millimeter': 1e-06, 'gal': 3.785411784, 'gallon': 3.785411784, 'gallons': 3.785411784, 'qt': 0.946352946, 'quart': 0.946352946, 'quarts': 0.946352946, 'pt': 0.473176473, 'pint': 0.473176473, 'pints': 0.473176473, 'cup': 0.2365882365, 'cups': 0.2365882365, 'fl_oz': 0.0295735295625, 'fluid ounce': 0.0295735295625, 'fluid ounces': 0.0295735295625}
    if unit_lower not in factors:
        raise ValueError(f'Unsupported unit: {unit}')
    return value * factors[unit_lower]
if __name__ == '__main__':
    sample_values = [(1.0, 'l'), (500.0, 'ml'), (1.0, 'gal'), (1.0, 'qt'), (1.0, 'pt'), (1.0, 'cup'), (1.0, 'fl_oz'), (1.0, 'm3'), (1.0, 'cm3'), (1.0, 'mm3')]
    for val, unit in sample_values:
        result = convert_volume_to_liters(val, unit)
        print(f'{val} {unit} = {result} liters')