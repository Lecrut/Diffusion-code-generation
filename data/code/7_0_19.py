def convert_time(value, source_unit, target_unit):
    conversion_factors = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600
    }
    
    source_unit_lower = source_unit.lower()
    target_unit_lower = target_unit.lower()
    
    if source_unit_lower not in conversion_factors:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    if target_unit_lower not in conversion_factors:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    
    value_in_seconds = value * conversion_factors[source_unit_lower]
    result = value_in_seconds / conversion_factors[target_unit_lower]
    return result

if __name__ == '__main__':
    print(convert_time(2, 'hours', 'minutes'))
    print(convert_time(90, 'seconds', 'minutes'))
    print(convert_time(120, 'minutes', 'hours'))
    print(convert_time(1, 'hours', 'seconds'))