def convert_volume(value, source_unit, target_unit='liters'):
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    if value < 0:
        raise ValueError("Volume cannot be negative")
    if not isinstance(source_unit, str) or not isinstance(target_unit, str):
        raise TypeError("Units must be strings")

    source_unit = source_unit.lower().strip()
    target_unit = target_unit.lower().strip()

    conversion_to_liters = {
        'liters': 1.0,
        'liter': 1.0,
        'l': 1.0,
        'milliliters': 0.001,
        'milliliter': 0.001,
        'ml': 0.001,
        'gallons': 3.78541,
        'gallon': 3.78541,
        'gal': 3.78541,
        'quarts': 0.946353,
        'quart': 0.946353,
        'qt': 0.946353,
        'pints': 0.473176,
        'pint': 0.473176,
        'pt': 0.473176,
        'cups': 0.236588,
        'cup': 0.236588,
        'fluid_ounces': 0.0295735,
        'fluid_ounce': 0.0295735,
        'fl_oz': 0.0295735,
        'tablespoons': 0.0147868,
        'tablespoon': 0.0147868,
        'tbsp': 0.0147868,
        'teaspoons': 0.00492892,
        'teaspoon': 0.00492892,
        'tsp': 0.00492892,
        'cubic_meters': 1000.0,
        'cubic_meter': 1000.0,
        'm3': 1000.0,
        'cubic_feet': 28.3168,
        'cubic_foot': 28.3168,
        'ft3': 28.3168,
        'cubic_inches': 0.0163871,
        'cubic_inch': 0.0163871,
        'in3': 0.0163871,
    }

    if source_unit not in conversion_to_liters:
        raise ValueError(f"Unknown source unit: {source_unit}")
    if target_unit not in conversion_to_liters:
        raise ValueError(f"Unknown target unit: {target_unit}")

    liters = value * conversion_to_liters[source_unit]
    result = liters / conversion_to_liters[target_unit]

    return result

if __name__ == '__main__':
    print(convert_volume(1, 'gallons', 'liters'))
    print(convert_volume(500, 'ml', 'liters'))
    print(convert_volume(2, 'liters', 'cups'))
    print(convert_volume(1, 'm3', 'gallons'))
    print(convert_volume(10, 'cups', 'ml'))