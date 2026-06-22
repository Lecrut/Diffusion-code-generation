def convert_volume_to_liters(value: float, unit: str) -> float:
    conversion_factors = {
        'l': 1.0,
        'liter': 1.0,
        'liters': 1.0,
        'ml': 0.001,
        'milliliter': 0.001,
        'milliliters': 0.001,
        'gal': 3.785411784,
        'gallon': 3.785411784,
        'gallons': 3.785411784,
        'fl oz': 0.0295735295625,
        'fluid ounce': 0.0295735295625,
        'fluid ounces': 0.0295735295625,
        'pt': 0.473176473,
        'pint': 0.473176473,
        'pints': 0.473176473,
        'qt': 0.946352946,
        'quart': 0.946352946,
        'quarts': 0.946352946,
        'cup': 0.2365882365,
        'cups': 0.2365882365,
        'tbsp': 0.01478676478125,
        'tablespoon': 0.01478676478125,
        'tablespoons': 0.01478676478125,
        'tsp': 0.00492892159375,
        'teaspoon': 0.00492892159375,
        'teaspoons': 0.00492892159375,
        'm3': 1000.0,
        'cubic meter': 1000.0,
        'cubic meters': 1000.0,
        'cm3': 0.001,
        'cubic centimeter': 0.001,
        'cubic centimeters': 0.001,
        'in3': 0.016387064,
        'cubic inch': 0.016387064,
        'cubic inches': 0.016387064,
        'ft3': 28.316846592,
        'cubic foot': 28.316846592,
        'cubic feet': 28.316846592,
        'bbl': 158.987294928,
        'barrel': 158.987294928,
        'barrels': 158.987294928,
        'imp gal': 4.54609,
        'imperial gallon': 4.54609,
        'imperial gallons': 4.54609,
        'imp pt': 0.56826125,
        'imperial pint': 0.56826125,
        'imperial pints': 0.56826125,
    }
    normalized_unit = unit.strip().lower().replace(' ', '')
    if normalized_unit in conversion_factors:
        return value * conversion_factors[normalized_unit]
    raise ValueError(f"Unsupported volume unit: {unit}")

if __name__ == '__main__':
    print(convert_volume_to_liters(1, 'gal'))
    print(convert_volume_to_liters(500, 'ml'))
    print(convert_volume_to_liters(1, 'l'))
    print(convert_volume_to_liters(1.5, 'cups'))
    print(convert_volume_to_liters(2, 'qt'))
    print(convert_volume_to_liters(1, 'm3'))
    print(convert_volume_to_liters(1, 'bbl'))
    print(convert_volume_to_liters(1, 'imp gal'))
    print(convert_volume_to_liters(100, 'fl oz'))