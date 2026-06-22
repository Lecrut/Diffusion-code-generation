def convert_volume(value, source_unit, target_unit='liters'):
    units = {
        'liters': 1.0,
        'milliliters': 0.001,
        'cubic_meters': 1000.0,
        'gallons_us': 3.78541,
        'quarts_us': 0.946353,
        'pints_us': 0.473176,
        'cups_us': 0.236588,
        'fluid_ounces_us': 0.0295735,
        'liters_imperial': 1.0,
        'gallons_uk': 4.54609,
        'quarts_uk': 1.13652,
        'pints_uk': 0.568261,
    }
    
    source_lower = source_unit.lower()
    target_lower = target_unit.lower()
    
    if source_lower not in units:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    if target_lower not in units:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    
    value_in_liters = value * units[source_lower]
    result = value_in_liters / units[target_lower]
    return result

if __name__ == '__main__':
    val = 2.5
    src = 'gallons_us'
    tgt = 'liters'
    res = convert_volume(val, src, tgt)
    print(res)