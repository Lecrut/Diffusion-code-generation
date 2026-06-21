def convert_volume(value, source_unit, target_unit='m3'):
    base_units = {
        'ml': 0.000001,
        'l': 0.001,
        'm3': 1.0,
        'ft3': 0.0283168,
        'gal_us': 0.00378541,
        'qt_us': 0.000946353,
        'pt_us': 0.000473176,
        'cup_us': 0.000236588,
        'tbsp_us': 0.0000147868,
        'tsp_us': 0.00000492892,
        'in3': 0.0000163871,
        'gal_uk': 0.00454609,
        'qt_uk': 0.00113652,
        'pt_uk': 0.000568264,
        'cup_uk': 0.000284131,
        'tbsp_uk': 0.0000177582,
        'tsp_uk': 0.00000591939
    }
    
    source_unit_lower = source_unit.lower()
    target_unit_lower = target_unit.lower()
    
    if source_unit_lower not in base_units:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    if target_unit_lower not in base_units:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    
    value_in_m3 = value * base_units[source_unit_lower]
    result = value_in_m3 / base_units[target_unit_lower]
    return result

if __name__ == '__main__':
    result1 = convert_volume(1000, 'ml', 'l')
    result2 = convert_volume(1, 'm3', 'gal_us')
    result3 = convert_volume(5, 'gal_us', 'l')
    print(result1)
    print(result2)
    print(result3)