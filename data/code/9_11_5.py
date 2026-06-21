def convert_volume(value, source_unit, target_unit='mL'):
    units_to_ml = {
        'ml': 1.0,
        'milliliter': 1.0,
        'milliliters': 1.0,
        'l': 1000.0,
        'liter': 1000.0,
        'liters': 1000.0,
        'cl': 10.0,
        'centiliter': 10.0,
        'centiliters': 10.0,
        'dl': 100.0,
        'deciliter': 100.0,
        'deciliters': 100.0,
        'tsp': 4.92892159,
        'teaspoon': 4.92892159,
        'teaspoons': 4.92892159,
        'tbsp': 14.7867648,
        'tablespoon': 14.7867648,
        'tablespoons': 14.7867648,
        'fl oz': 29.5735296,
        'fluid ounce': 29.5735296,
        'fluid ounces': 29.5735296,
        'cup': 236.588236,
        'cups': 236.588236,
        'pt': 473.176473,
        'pint': 473.176473,
        'pints': 473.176473,
        'qt': 946.352946,
        'quart': 946.352946,
        'quarts': 946.352946,
        'gal': 3785.41178,
        'gallon': 3785.41178,
        'gallons': 3785.41178,
        'm3': 1000000.0,
        'cubic meter': 1000000.0,
        'cubic meters': 1000000.0,
        'in3': 16.387064,
        'cubic inch': 16.387064,
        'cubic inches': 16.387064,
        'ft3': 28316.8466,
        'cubic foot': 28316.8466,
        'cubic feet': 28316.8466,
    }
    
    source_unit = source_unit.lower().strip()
    target_unit = target_unit.lower().strip()
    
    if source_unit not in units_to_ml:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    if target_unit not in units_to_ml:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    
    if not isinstance(value, (int, float)):
        raise TypeError("Volume value must be a number")
    if value < 0:
        raise ValueError("Volume value cannot be negative")
    
    value_in_ml = value * units_to_ml[source_unit]
    result = value_in_ml / units_to_ml[target_unit]
    return result

if __name__ == '__main__':
    result1 = convert_volume(1, 'gal', 'l')
    print(result1)
    result2 = convert_volume(2, 'cup', 'ml')
    print(result2)
    result3 = convert_volume(1000, 'ml', 'l')
    print(result3)