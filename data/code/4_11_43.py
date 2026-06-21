def convert_distance(value, source_unit):
    M_TO_KM = 1 / 1000.0
    M_TO_MI = 1 / 1609.344
    M_TO_FT = 3.28084

    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a numeric type.")
    
    source_units = {
        'meters': 1.0,
        'kilometers': M_TO_KM,
        'miles': M_TO_MI,
        'feet': M_TO_FT
    }
    
    if source_unit not in source_units:
        raise ValueError(f"Unsupported unit: {source_unit}")
    
    meters = value * source_units[source_unit]
    
    conversions = {
        'meters': meters,
        'kilometers': meters / 1000.0,
        'miles': meters / 1609.344,
        'feet': meters / 0.3048
    }
    
    return round(conversions[source_unit], 6)

if __name__ == '__main__':
    print(convert_distance(50, 'meters'))
    print(convert_distance(2, 'kilometers'))
    print(convert_distance(1, 'miles'))
    print(convert_distance(3280.84, 'feet'))