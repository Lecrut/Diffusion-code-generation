def convert_volume(value, target_unit):
    units_to_liters = {
        'L': 1.0,
        'l': 1.0,
        'm3': 1000.0,
        'm^3': 1000.0,
        'gal': 3.78541,
        'gal_us': 3.78541,
        'qt': 0.946353,
        'pt': 0.473176,
        'cup': 0.236588,
        'fl_oz': 0.0295735,
        'tbsp': 0.0147868,
        'tsp': 0.00492892,
    }
    
    if target_unit not in units_to_liters:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    
    source_unit = value[0]
    numeric_value = value[1]
    
    if source_unit not in units_to_liters:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    
    liters = numeric_value * units_to_liters[source_unit]
    result = liters / units_to_liters[target_unit]
    return result

if __name__ == '__main__':
    sample_data = [
        ('m3', 1),
        ('gal_us', 10),
        ('L', 500),
    ]
    target = 'L'
    for src, val in sample_data:
        res = convert_volume((src, val), target)
        print(f"{val} {src} = {res} {target}")
    print(f"{sample_data[0][1]} {sample_data[0][0]} converted to m3: {convert_volume((sample_data[0][0], sample_data[0][1]), 'm3')}")