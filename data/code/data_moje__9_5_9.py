def convert_volume_to_liters(value, unit):
    unit = unit.lower().strip()
    conversion_factors = {'liter': 1.0, 'liters': 1.0, 'l': 1.0, 'milliliter': 0.001, 'milliliters': 0.001, 'ml': 0.001, 'milliliter': 0.001, 'kiloliter': 1000.0, 'kiloliters': 1000.0, 'kl': 1000.0, 'centiliter': 0.01, 'centiliters': 0.01, 'cl': 0.01, 'deciliter': 0.1, 'deciliters': 0.1, 'dl': 0.1, 'gallon': 3.785411784, 'gallons': 3.785411784, 'gal': 3.785411784, 'quart': 0.946352946, 'quarts': 0.946352946, 'qt': 0.946352946, 'pint': 0.473176473, 'pints': 0.473176473, 'pt': 0.473176473, 'cup': 0.2365882365, 'cups': 0.2365882365, 'tablespoon': 0.01478676478125, 'tablespoons': 0.01478676478125, 'tbsp': 0.01478676478125, 'teaspoon': 0.00492892159375, 'teaspoons': 0.00492892159375, 'tsp': 0.00492892159375, 'fluid ounce': 0.0295735295625, 'fluid ounces': 0.0295735295625, 'floz': 0.0295735295625, 'cubic meter': 1000.0, 'cubic meters': 1000.0, 'm3': 1000.0, 'cubic centimeter': 0.001, 'cubic centimeters': 0.001, 'cc': 0.001, 'cm3': 0.001, 'cubic millimeter': 1e-06, 'cubic millimeters': 1e-06, 'mm3': 1e-06, 'cubic foot': 28.316846592, 'cubic feet': 28.316846592, 'ft3': 28.316846592, 'cubic inch': 0.016387064, 'cubic inches': 0.016387064, 'in3': 0.016387064}
    if unit not in conversion_factors:
        raise ValueError(f'Unsupported unit: {unit}')
    return value * conversion_factors[unit]
if __name__ == '__main__':
    gallons_value = 1.0
    liters_result = convert_volume_to_liters(gallons_value, 'gallon')
    print(liters_result)
    milliliters_value = 1000.0
    liters_from_ml = convert_volume_to_liters(milliliters_value, 'ml')
    print(liters_from_ml)
    cubic_feet_value = 1.0
    liters_from_cf = convert_volume_to_liters(cubic_feet_value, 'cubic foot')
    print(liters_from_cf)