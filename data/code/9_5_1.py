def convert_volume(value, from_unit):
    conversions = {
        'liters': 1.0,
        'liter': 1.0,
        'l': 1.0,
        'milliliters': 1e-3,
        'milliliter': 1e-3,
        'ml': 1e-3,
        'centiliters': 1e-2,
        'centiliter': 1e-2,
        'cl': 1e-2,
        'deciliters': 1e-1,
        'deciliter': 1e-1,
        'dl': 1e-1,
        'kiloliters': 1e3,
        'kiloliter': 1e3,
        'kl': 1e3,
        'microliters': 1e-6,
        'microliter': 1e-6,
        'ul': 1e-6,
        'nanoliters': 1e-9,
        'nanoliter': 1e-9,
        'nl': 1e-9,
        'gallons_us': 3.785411784,
        'gallon_us': 3.785411784,
        'gal_us': 3.785411784,
        'gallons_uk': 4.54609,
        'gallon_uk': 4.54609,
        'gal_uk': 4.54609,
        'cups_us': 0.2365882365,
        'cup_us': 0.2365882365,
        'pints_us': 0.473176473,
        'pint_us': 0.473176473,
        'quarts_us': 0.946352946,
        'quart_us': 0.946352946,
        'fluid_ounces_us': 0.0295735295625,
        'fluid_ounce_us': 0.0295735295625,
        'floz_us': 0.0295735295625,
        'tablespoons_us': 0.01478676478125,
        'tablespoon_us': 0.01478676478125,
        'tbsp_us': 0.01478676478125,
        'teaspoons_us': 0.00492892159375,
        'teaspoon_us': 0.00492892159375,
        'tsp_us': 0.00492892159375,
        'cubic_meters': 1000.0,
        'cubic_meter': 1000.0,
        'm3': 1000.0,
        'cubic_centimeters': 1e-3,
        'cubic_centimeter': 1e-3,
        'cc': 1e-3,
        'cm3': 1e-3,
        'cubic_inches': 0.016387064,
        'cubic_inch': 0.016387064,
        'in3': 0.016387064,
        'cubic_feet': 28.316846592,
        'cubic_foot': 28.316846592,
        'ft3': 28.316846592,
    }
    
    unit_key = from_unit.lower().strip()
    
    if unit_key not in conversions:
        raise ValueError(f"Unsupported unit: {from_unit}")
    
    factor = conversions[unit_key]
    return value * factor

if __name__ == '__main__':
    print(convert_volume(1, 'gallon_us'))
    print(convert_volume(1000, 'milliliters'))
    print(convert_volume(1, 'cubic_meter'))
    print(convert_volume(16, 'fluid_ounces_us'))