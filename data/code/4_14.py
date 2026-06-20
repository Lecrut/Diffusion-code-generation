def convert_distance(value, source_unit, target_unit):
    units = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'mile': 1609.344,
        'foot': 0.3048
    }
    
    valid_sources = {'meter', 'meters', 'kilometer', 'kilometers', 'mile', 'miles', 'foot', 'feet'}
    valid_targets = {'meter', 'meters', 'kilometer', 'kilometers', 'mile', 'miles', 'foot', 'feet'}
    
    source_key = source_unit.lower()
    target_key = target_unit.lower()
    
    if source_key not in valid_sources:
        raise ValueError(f"Invalid source unit: {source_unit}")
    if target_key not in valid_targets:
        raise ValueError(f"Invalid target unit: {target_unit}")
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    
    base_meters = value * units[source_key]
    result = base_meters / units[target_key]
    return round(result, 6)

if __name__ == '__main__':
    print(convert_distance(1, 'mile', 'kilometer'))
    print(convert_distance(1000, 'meter', 'foot'))
    print(convert_distance(5, 'kilometer', 'mile'))
    print(convert_distance(1, 'foot', 'meter'))