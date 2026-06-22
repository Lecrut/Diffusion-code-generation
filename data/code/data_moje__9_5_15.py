def convert_to_liters(value, unit):
    if not isinstance(value, (int, float)):
        raise TypeError('Value must be a number.')
    conversion_factors = {'liter': 1.0, 'litre': 1.0, 'l': 1.0, 'ml': 0.001, 'milliliter': 0.001, 'millilitre': 0.001, 'us_gallon': 3.785411784, 'us_gal': 3.785411784, 'us_fl_oz': 0.0295735295625, 'us_cup': 0.2365882365, 'us_pt': 0.473176473, 'us_pint': 0.473176473, 'us_quart': 0.946352946, 'us_tbsp': 0.01478676478125, 'us_tsp': 0.00492892159375, 'imp_gallon': 4.54609, 'imp_gal': 4.54609, 'imp_fl_oz': 0.0284130625, 'imp_cup': 0.284130625, 'imp_pt': 0.56826125, 'imp_pint': 0.56826125, 'imp_quart': 1.1365225, 'imp_tbsp': 0.0177581640625, 'imp_tsp': 0.005919388020833333, 'm3': 1000.0, 'cubic_meter': 1000.0, 'cm3': 0.001, 'cubic_centimeter': 0.001, 'mm3': 1e-06, 'cubic_millimeter': 1e-06, 'dl': 0.1, 'deciliter': 0.1, 'cl': 0.01, 'centiliter': 0.01}
    normalized_unit = unit.lower().strip()
    if normalized_unit in conversion_factors:
        return value * conversion_factors[normalized_unit]
    else:
        raise ValueError(f'Unsupported unit: {unit}')
if __name__ == '__main__':
    test_cases = [(1, 'liter'), (1000, 'ml'), (1, 'us_gallon'), (1, 'imp_gallon'), (1, 'm3'), (500, 'cm3'), (8, 'us_fl_oz'), (2, 'us_cup'), (1, 'dl'), (250, 'cl')]
    for value, unit in test_cases:
        result = convert_to_liters(value, unit)
        print(f'{value} {unit} = {result} liters')