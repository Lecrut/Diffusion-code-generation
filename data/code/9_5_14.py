def convert_volume_to_liters(value: float, unit: str) -> float:
    unit_lower = unit.strip().lower()
    conversion_factors = {'l': 1.0, 'liter': 1.0, 'litres': 1.0, 'milliliter': 0.001, 'millilitre': 0.001, 'ml': 0.001, 'gigaliter': 1000000000.0, 'gl': 1000000000.0, 'kiloliter': 1000.0, 'kl': 1000.0, 'hectoliter': 100.0, 'hl': 100.0, 'decaliter': 10.0, 'dal': 10.0, 'deciliter': 0.1, 'dl': 0.1, 'centiliter': 0.01, 'cl': 0.01, 'microliter': 1e-06, 'ul': 1e-06, 'gal': 3.785411784, 'gallon': 3.785411784, 'qt': 0.946352946, 'quart': 0.946352946, 'pt': 0.473176473, 'pint': 0.473176473, 'cup': 0.2365882365, 'fl_oz': 0.0295735295625, 'fluid_ounce': 0.0295735295625, 'tsp': 0.00492892159375, 'teaspoon': 0.00492892159375, 'tbsp': 0.01478676478125, 'tablespoon': 0.01478676478125, 'ft3': 28.316846592, 'cubic_foot': 28.316846592, 'in3': 0.016387064, 'cubic_inch': 0.016387064, 'yd3': 764.554857984, 'cubic_yard': 764.554857984, 'm3': 1000.0, 'cubic_meter': 1000.0, 'cm3': 0.001, 'cubic_centimeter': 0.001}
    if unit_lower not in conversion_factors:
        raise ValueError(f'Unsupported unit: {unit}')
    return value * conversion_factors[unit_lower]
if __name__ == '__main__':
    result_gal = convert_volume_to_liters(1, 'gal')
    print(result_gal)
    result_lit = convert_volume_to_liters(1, 'liter')
    print(result_lit)
    result_ml = convert_volume_to_liters(1000, 'ml')
    print(result_ml)
    result_m3 = convert_volume_to_liters(1, 'm3')
    print(result_m3)
    result_cup = convert_volume_to_liters(1, 'cup')
    print(result_cup)