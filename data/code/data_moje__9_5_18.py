def convert_volume_to_liters(value, unit):
    conversion_factors = {
        'liter': 1.0,
        'litre': 1.0,
        'l': 1.0,
        'ml': 0.001,
        'milliliter': 0.001,
        'millilitre': 0.001,
        'm3': 1000.0,
        'cubic_meter': 1000.0,
        'cubic_centimeter': 0.001,
        'cc': 0.001,
        'gal': 3.785411784,
        'gallon': 3.785411784,
        'us_gallon': 3.785411784,
        'qt': 0.946352946,
        'quart': 0.946352946,
        'pt': 0.473176473,
        'pint': 0.473176473,
        'cup': 0.2365882365,
        'fl_oz': 0.0295735295625,
        'fluid_ounce': 0.0295735295625,
        'tbsp': 0.01478676478125,
        'tablespoon': 0.01478676478125,
        'tsp': 0.00492892159375,
        'teaspoon': 0.00492892159375,
        'imperial_gallon': 4.54609,
        'uk_gallon': 4.54609,
        'imperial_quart': 1.1365225,
        'uk_quart': 1.1365225,
        'imperial_pint': 0.56826125,
        'uk_pint': 0.56826125,
        'imperial_fl_oz': 0.0284130625,
        'uk_fl_oz': 0.0284130625,
        'barrel': 119.240471196,
        'oil_barrel': 158.987294928,
        'bbl': 158.987294928,
        'cubic_foot': 28.316846592,
        'ft3': 28.316846592,
        'cubic_inch': 0.016387064,
        'in3': 0.016387064
    }
    
    normalized_unit = unit.lower().replace(' ', '_')
    
    if normalized_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    factor = conversion_factors[normalized_unit]
    return value * factor

if __name__ == '__main__':
    print(convert_volume_to_liters(1, 'gallon'))
    print(convert_volume_to_liters(500, 'ml'))
    print(convert_volume_to_liters(2, 'liter'))
    print(convert_volume_to_liters(1, 'imperial_gallon'))
    print(convert_volume_to_liters(16, 'fluid_ounce'))
    print(convert_volume_to_liters(1, 'cubic_foot'))
    print(convert_volume_to_liters(3, 'cup'))