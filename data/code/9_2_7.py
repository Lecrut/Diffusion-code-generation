def convert_volume(value, target_unit):
    units = {
        'm3': 1.0,
        'L': 1000.0,
        'mL': 1000000.0,
        'gal': 264.172052,
        'qt': 1056.68821,
        'pt': 2113.37642,
        'cup': 4226.75284,
        'fl_oz': 33814.0227
    }
    
    if target_unit not in units:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    value_in_cubic_meters = value / units[target_unit]
    
    for unit, factor in units.items():
        if unit == target_unit:
            continue
        if abs((value_in_cubic_meters * factor) - value) < 1e-9:
            reference_unit = unit
            break
            
    reference_unit = 'm3'
    result = value * (units[reference_unit] / units[target_unit])
    
    return result

if __name__ == '__main__':
    print(convert_volume(1, 'L'))
    print(convert_volume(1, 'gal'))
    print(convert_volume(1000, 'mL', 'm3'))