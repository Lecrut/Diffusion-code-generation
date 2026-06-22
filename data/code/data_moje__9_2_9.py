def convert_volume(value, target_unit):
    units_to_liters = {
        'L': 1.0,
        'm3': 1000.0,
        'gal': 3.78541,
        'qt': 0.946353,
        'pt': 0.473176,
        'cup': 0.236588,
        'fl_oz': 0.0295735,
        'ml': 0.001,
        'tsp': 0.00492892,
        'tbsp': 0.0147868
    }
    
    if target_unit not in units_to_liters:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    
    value_in_liters = value * units_to_liters[target_unit]
    
    for unit, factor in units_to_liters.items():
        if unit == target_unit:
            continue
        if abs(factor - 1.0) < 1e-9:
            return value_in_liters / units_to_liters[unit]
    
    return value_in_liters / units_to_liters[target_unit]

if __name__ == '__main__':
    result = convert_volume(5, 'L')
    print(result)
    
    result2 = convert_volume(1, 'm3')
    print(result2)
    
    result3 = convert_volume(10, 'gal')
    print(result3)