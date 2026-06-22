def convert_to_liters(volume: float, unit: str) -> float:
    factors = {
        'liter': 1.0,
        'liters': 1.0,
        'l': 1.0,
        'milliliter': 0.001,
        'milliliters': 0.001,
        'ml': 0.001,
        'cubic meter': 1000.0,
        'cubic meters': 1000.0,
        'm3': 1000.0,
        'cubic centimeter': 0.001,
        'cubic centimeters': 0.001,
        'cm3': 0.001,
        'cubic inch': 0.016387064,
        'cubic inches': 0.016387064,
        'in3': 0.016387064,
        'cubic foot': 28.316846592,
        'cubic feet': 28.316846592,
        'ft3': 28.316846592,
        'cubic yard': 764.554857984,
        'cubic yards': 764.554857984,
        'yd3': 764.554857984,
        'teaspoon': 0.00492892159375,
        'teaspoons': 0.00492892159375,
        'tsp': 0.00492892159375,
        'tablespoon': 0.01478676478125,
        'tablespoons': 0.01478676478125,
        'tbsp': 0.01478676478125,
        'fluid ounce': 0.0295735295625,
        'fluid ounces': 0.0295735295625,
        'fl oz': 0.0295735295625,
        'cup': 0.2365882365,
        'cups': 0.2365882365,
        'pint': 0.473176473,
        'pints': 0.473176473,
        'quart': 0.946352946,
        'quarts': 0.946352946,
        'gallon': 3.785411784,
        'gallons': 3.785411784,
        'imperial teaspoon': 0.00591938802083,
        'imperial teaspoons': 0.00591938802083,
        'imp tsp': 0.00591938802083,
        'imperial tablespoon': 0.0177581640625,
        'imperial tablespoons': 0.0177581640625,
        'imp tbsp': 0.0177581640625,
        'imperial fluid ounce': 0.0284130625,
        'imperial fluid ounces': 0.0284130625,
        'imp fl oz': 0.0284130625,
        'imperial cup': 0.284130625,
        'imperial cups': 0.284130625,
        'imp cup': 0.284130625,
        'imperial pint': 0.56826125,
        'imperial pints': 0.56826125,
        'imp pt': 0.56826125,
        'imperial quart': 1.1365225,
        'imperial quarts': 1.1365225,
        'imp qt': 1.1365225,
        'imperial gallon': 4.54609,
        'imperial gallons': 4.54609,
        'imp gal': 4.54609,
    }
    unit_lower = unit.lower().strip()
    if unit_lower not in factors:
        raise ValueError(f"Unsupported unit: {unit}")
    return volume * factors[unit_lower]

if __name__ == '__main__':
    print(convert_to_liters(1, 'gallon'))
    print(convert_to_liters(1000, 'ml'))
    print(convert_to_liters(1, 'cubic meter'))
    print(convert_to_liters(16, 'cubic inches'))
    print(convert_to_liters(2, 'imperial gallon'))