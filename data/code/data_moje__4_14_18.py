def convert_distance(value, unit):
    valid_units = {
        'm': 1.0,
        'km': 1000.0,
        'mi': 1609.344,
        'ft': 0.3048
    }
    
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    
    if not isinstance(unit, str):
        raise TypeError("Unit must be a string")
    
    normalized_unit = unit.lower().strip()
    
    if normalized_unit not in valid_units:
        raise ValueError(f"Unsupported unit: {unit}")
    
    meters = value * valid_units[normalized_unit]
    return round(meters, 6)

if __name__ == '__main__':
    result_m_to_km = convert_distance(1000, 'm')
    print(result_m_to_km)
    
    result_km_to_mi = convert_distance(1, 'km')
    print(result_km_to_mi)
    
    result_mi_to_ft = convert_distance(1, 'mi')
    print(result_mi_to_ft)
    
    result_ft_to_m = convert_distance(5280, 'ft')
    print(result_ft_to_m)