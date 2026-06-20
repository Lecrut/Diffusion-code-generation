def convert_distance(value, from_unit, to_unit):
    conversion_factors = {
        'meters': {'meters': 1.0, 'kilometers': 0.001, 'miles': 0.000621371},
        'kilometers': {'meters': 1000.0, 'kilometers': 1.0, 'miles': 0.621371},
        'miles': {'meters': 1609.34, 'kilometers': 1.60934, 'miles': 1.0}
    }
    
    if value < 0:
        raise ValueError("Distance cannot be negative")
    
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    
    if from_unit_lower not in conversion_factors:
        raise ValueError(f"Unsupported from_unit: {from_unit}")
    
    if to_unit_lower not in conversion_factors:
        raise ValueError(f"Unsupported to_unit: {to_unit}")
    
    converted_value = value * conversion_factors[from_unit_lower][to_unit_lower]
    
    return round(converted_value, 6)

if __name__ == '__main__':
    sample_conversions = [
        (1000, 'meters', 'kilometers'),
        (5, 'kilometers', 'meters'),
        (1, 'miles', 'kilometers'),
        (1609.34, 'meters', 'miles'),
        (0, 'kilometers', 'meters'),
        (2.5, 'miles', 'meters')
    ]
    
    for val, from_u, to_u in sample_conversions:
        result = convert_distance(val, from_u, to_u)
        print(f"{val} {from_u} = {result} {to_u}")