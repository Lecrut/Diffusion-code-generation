def convert_volume(value, source_unit, target_unit='mL'):
    conversion_rates = {
        'mL': 1.0,
        'L': 1000.0,
        'gal': 3785.411784,
        'qt': 946.352946,
        'pt': 473.176473,
        'cup': 236.5882365,
        'fl_oz': 29.5735295625,
        'tbsp': 14.78676478125,
        'tsp': 4.92892159375,
        'm3': 1000000.0,
        'cm3': 1.0
    }
    
    source_unit_lower = source_unit.lower()
    target_unit_lower = target_unit.lower()
    
    if source_unit_lower not in conversion_rates:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    if target_unit_lower not in conversion_rates:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    
    base_value = value * conversion_rates[source_unit_lower]
    result = base_value / conversion_rates[target_unit_lower]
    return result

if __name__ == '__main__':
    print(convert_volume(1, 'gal', 'L'))
    print(convert_volume(2, 'L', 'mL'))
    print(convert_volume(16, 'tbsp', 'fl_oz'))
    print(convert_volume(3, 'qt', 'gal'))