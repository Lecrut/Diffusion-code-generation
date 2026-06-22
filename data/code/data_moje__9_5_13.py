def convert_to_liters(value: float, unit: str) -> float:
    unit = unit.lower().strip()
    conversion_factors = {'ml': 0.001, 'l': 1.0, 'kl': 1000.0, 'gal': 3.785411784, 'qt': 0.946352946, 'pt': 0.473176473, 'cup': 0.2365882365, 'fl_oz': 0.0295735295625, 'tsp': 0.00492892159375, 'tbsp': 0.01478676478125, 'in3': 0.016387064, 'ft3': 28.316846592, 'm3': 1000.0, 'cm3': 0.001, 'yd3': 764.554857984}
    if unit not in conversion_factors:
        raise ValueError(f'Unsupported unit: {unit}')
    return value * conversion_factors[unit]
if __name__ == '__main__':
    result_ml = convert_to_liters(1000, 'ml')
    print(f'1000 ml = {result_ml} liters')
    result_gal = convert_to_liters(1, 'gal')
    print(f'1 gal = {result_gal} liters')
    result_l = convert_to_liters(5.5, 'l')
    print(f'5.5 l = {result_l} liters')
    result_m3 = convert_to_liters(1, 'm3')
    print(f'1 m3 = {result_m3} liters')
    result_ft3 = convert_to_liters(10, 'ft3')
    print(f'10 ft3 = {result_ft3} liters')
    result_cup = convert_to_liters(8, 'cup')
    print(f'8 cup = {result_cup} liters')