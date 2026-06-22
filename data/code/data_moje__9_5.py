def convert_volume_to_liters(value, unit):
    unit = unit.lower()
    conversion_factors = {
        'liter': 1.0,
        'l': 1.0,
        'milliliter': 0.001,
        'ml': 0.001,
        'microliter': 0.000001,
        'ul': 0.000001,
        'cubic_meter': 1000.0,
        'm3': 1000.0,
        'cubic_decimeter': 1.0,
        'dm3': 1.0,
        'cubic_centimeter': 0.001,
        'cm3': 0.001,
        'cubic_inch': 0.016387064,
        'in3': 0.016387064,
        'cubic_foot': 28.316846592,
        'ft3': 28.316846592,
        'cubic_yard': 764.554857984,
        'yd3': 764.554857984,
        'teaspoon': 0.00492892159375,
        'tsp': 0.00492892159375,
        'tablespoon': 0.01478676478125,
        'tbsp': 0.01478676478125,
        'fluid_ounce_us': 0.0295735295625,
        'floz_us': 0.0295735295625,
        'cup_us': 0.2365882365,
        'cup': 0.2365882365,
        'pint_us': 0.473176473,
        'pt_us': 0.473176473,
        'quart_us': 0.946352946,
        'qt_us': 0.946352946,
        'gallon_us': 3.785411784,
        'gal_us': 3.785411784,
        'fluid_ounce_uk': 0.0284130625,
        'floz_uk': 0.0284130625,
        'pint_uk': 0.56826125,
        'pt_uk': 0.56826125,
        'quart_uk': 1.1365225,
        'qt_uk': 1.1365225,
        'gallon_uk': 4.54609,
        'gal_uk': 4.54609,
        'barrel_oil': 158.987294928,
        'bbl_oil': 158.987294928,
        'barrel_beer': 117.3477658,
        'bbl_beer': 117.3477658,
    }
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    return value * conversion_factors[unit]

if __name__ == '__main__':
    print(convert_volume_to_liters(1, 'gallon_us'))
    print(convert_volume_to_liters(100, 'ml'))
    print(convert_volume_to_liters(5, 'cubic_foot'))
    print(convert_volume_to_liters(1, 'liter'))
    print(convert_volume_to_liters(2, 'barrel_oil'))