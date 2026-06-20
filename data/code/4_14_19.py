def convert_distance(value, source_unit):
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a number")
    if isinstance(value, bool):
        raise ValueError("Value must be a number")
    if not isinstance(source_unit, str):
        raise TypeError("Source unit must be a string")
    
    valid_units = ('meters', 'kilometers', 'miles', 'feet')
    source_unit_lower = source_unit.lower()
    if source_unit_lower not in valid_units:
        raise ValueError(f"Source unit must be one of {valid_units}")
    
    meters = _to_meters(value, source_unit_lower)
    
    results = {}
    for unit in valid_units:
        results[unit] = _from_meters(meters, unit)
    
    return results

def _to_meters(value, source_unit):
    if source_unit == 'meters':
        return float(value)
    elif source_unit == 'kilometers':
        return float(value) * 1000.0
    elif source_unit == 'miles':
        return float(value) * 1609.344
    elif source_unit == 'feet':
        return float(value) * 0.3048
    else:
        raise ValueError("Unsupported source unit")

def _from_meters(meters, target_unit):
    if target_unit == 'meters':
        return round(float(meters), 6)
    elif target_unit == 'kilometers':
        return round(float(meters) / 1000.0, 6)
    elif target_unit == 'miles':
        return round(float(meters) / 1609.344, 6)
    elif target_unit == 'feet':
        return round(float(meters) / 0.3048, 6)
    else:
        raise ValueError("Unsupported target unit")

if __name__ == '__main__':
    result1 = convert_distance(1000, 'meters')
    print(result1)
    
    result2 = convert_distance(1, 'kilometers')
    print(result2)
    
    result3 = convert_distance(1, 'miles')
    print(result3)
    
    result4 = convert_distance(1, 'feet')
    print(result4)
    
    result5 = convert_distance(5280, 'feet')
    print(result5)
    
    result6 = convert_distance(0.621371, 'miles')
    print(result6)