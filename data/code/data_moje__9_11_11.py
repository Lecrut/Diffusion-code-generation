def convert_volume(value, source_unit, target_unit='liter'):
    units = {
        'liter': 1.0,
        'milliliter': 0.001,
        'gallon': 3.78541,
        'quart': 0.946353,
        'pint': 0.473176,
        'cup': 0.236588,
        'fluid_ounce': 0.0295735
    }
    
    source_unit_lower = source_unit.lower()
    target_unit_lower = target_unit.lower()
    
    if source_unit_lower not in units:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    
    if target_unit_lower not in units:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    
    value_in_liters = value * units[source_unit_lower]
    converted_value = value_in_liters / units[target_unit_lower]
    
    return converted_value

if __name__ == '__main__':
    sample_value = 5.0
    sample_source = 'gallon'
    sample_target = 'liter'
    result = convert_volume(sample_value, sample_source, sample_target)
    print(result)
    sample_source_2 = 'milliliter'
    sample_target_2 = 'cup'
    result_2 = convert_volume(500, sample_source_2, sample_target_2)
    print(result_2)