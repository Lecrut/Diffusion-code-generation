def convert_volume(volume, source_unit, target_unit='liter'):
    if not isinstance(volume, (int, float)):
        raise ValueError("Volume must be a number")
    if volume < 0:
        raise ValueError("Volume must be non-negative")
    if not isinstance(source_unit, str) or not isinstance(target_unit, str):
        raise ValueError("Units must be strings")

    source_lower = source_unit.lower().strip()
    target_lower = target_unit.lower().strip()

    conversion_rates = {
        'liter': 1.0,
        'litre': 1.0,
        'milliliter': 0.001,
        'millilitre': 0.001,
        'ml': 0.001,
        'cubic_meter': 1000.0,
        'cubic_centimeter': 0.001,
        'cubic_centimetre': 0.001,
        'cc': 0.001,
        'gallon': 3.78541,
        'us_gallon': 3.78541,
        'imperial_gallon': 4.54609,
        'quart': 0.946353,
        'pint': 0.473176,
        'cup': 0.24,
        'fluid_ounce': 0.0295735,
        'fl_oz': 0.0295735,
        'tablespoon': 0.0147868,
        'tbsp': 0.0147868,
        'teaspoon': 0.00492892,
        'tsp': 0.00492892,
        'barrel': 158.987,
        'bbl': 158.987,
        'cubic_foot': 28.3168,
        'ft3': 28.3168,
        'cubic_inch': 0.0163871,
        'in3': 0.0163871,
        'gallon_uk': 4.54609,
        'quart_uk': 1.13652,
        'pint_uk': 0.568261,
        'fluid_ounce_uk': 0.0284131,
        'tablespoon_uk': 0.0177582,
        'teaspoon_uk': 0.00591939
    }

    if source_lower not in conversion_rates:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    if target_lower not in conversion_rates:
        raise ValueError(f"Unsupported target unit: {target_unit}")

    volume_in_liters = volume * conversion_rates[source_lower]
    result = volume_in_liters / conversion_rates[target_lower]
    return result

if __name__ == '__main__':
    print(convert_volume(1, 'gallon', 'liter'))
    print(convert_volume(1000, 'ml', 'liter'))
    print(convert_volume(1, 'cubic_meter', 'liter'))
    print(convert_volume(5, 'liter', 'gallon'))
    print(convert_volume(2, 'pint', 'ml'))
    print(convert_volume(10, 'cubic_foot', 'liter'))
    print(convert_volume(100, 'fluid_ounce', 'ml'))
    print(convert_volume(0.5, 'imperial_gallon', 'liter'))
    print(convert_volume(1, 'cubic_inch', 'ml'))
    print(convert_volume(250, 'ml', 'cup'))