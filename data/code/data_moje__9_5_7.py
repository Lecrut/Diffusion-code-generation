def convert_to_liters(volume, unit):
    factors = {
        'ml': 0.001,
        'milliliter': 0.001,
        'milliliters': 0.001,
        'liter': 1.0,
        'litre': 1.0,
        'liters': 1.0,
        'litres': 1.0,
        'gallon': 3.785411784,
        'gallons': 3.785411784,
        'quart': 0.946352946,
        'quarts': 0.946352946,
        'pint': 0.473176473,
        'pints': 0.473176473,
        'cup': 0.2365882365,
        'cups': 0.2365882365,
        'fluid_ounce': 0.0295735295625,
        'fluid_ounces': 0.0295735295625,
        'ounce': 0.0295735295625,
        'ounces': 0.0295735295625,
        'tablespoon': 0.01478676478125,
        'tablespoons': 0.01478676478125,
        'teaspoon': 0.00492892159375,
        'teaspoons': 0.00492892159375,
        'cubic_meter': 1000.0,
        'cubic_meters': 1000.0,
        'cubic_centimeter': 0.001,
        'cubic_centimeters': 0.001,
        'cc': 0.001,
        'cm3': 0.001,
        'imperial_gallon': 4.54609,
        'imperial_gallons': 4.54609,
        'imperial_quart': 1.1365225,
        'imperial_quarts': 1.1365225,
        'imperial_pint': 0.56826125,
        'imperial_pints': 0.56826125,
        'imperial_fluid_ounce': 0.0284130625,
        'imperial_fluid_ounces': 0.0284130625,
    }
    unit_lower = unit.lower().strip()
    if unit_lower not in factors:
        raise ValueError(f"Unsupported unit: {unit}")
    return volume * factors[unit_lower]

if __name__ == '__main__':
    print(convert_to_liters(1, 'gallon'))
    print(convert_to_liters(1000, 'ml'))
    print(convert_to_liters(1, 'liter'))