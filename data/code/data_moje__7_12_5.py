def convert_time(value, from_unit, to_unit):
    units_to_seconds = {
        'second': 1,
        'minute': 60,
        'hour': 3600,
        'day': 86400,
        'week': 604800,
        'month': 2592000,
        'year': 31536000
    }
    
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    
    if from_unit_lower not in units_to_seconds:
        raise ValueError(f"Unsupported from_unit: {from_unit}")
    if to_unit_lower not in units_to_seconds:
        raise ValueError(f"Unsupported to_unit: {to_unit}")
    
    seconds = value * units_to_seconds[from_unit_lower]
    result = seconds / units_to_seconds[to_unit_lower]
    
    return result

if __name__ == '__main__':
    result1 = convert_time(1, 'hour', 'minute')
    print(result1)
    
    result2 = convert_time(24, 'day', 'second')
    print(result2)
    
    result3 = convert_time(1, 'year', 'month')
    print(result3)
    
    result4 = convert_time(3600, 'second', 'hour')
    print(result4)
    
    result5 = convert_time(1.5, 'week', 'day')
    print(result5)