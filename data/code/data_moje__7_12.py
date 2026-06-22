def convert_time(value, from_unit, to_unit):
    units_to_seconds = {
        'ms': 0.001,
        'second': 1,
        's': 1,
        'minute': 60,
        'm': 60,
        'hour': 3600,
        'h': 3600,
        'day': 86400,
        'd': 86400,
        'week': 604800,
        'wk': 604800,
        'month': 2592000,
        'mo': 2592000,
        'year': 31536000,
        'yr': 31536000
    }
    
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    
    if from_unit_lower not in units_to_seconds:
        raise ValueError(f"Unknown from_unit: {from_unit}")
    if to_unit_lower not in units_to_seconds:
        raise ValueError(f"Unknown to_unit: {to_unit}")
        
    seconds = value * units_to_seconds[from_unit_lower]
    converted = seconds / units_to_seconds[to_unit_lower]
    
    return converted

if __name__ == '__main__':
    result = convert_time(1, 'hour', 'minute')
    print(result)
    
    result2 = convert_time(120, 'second', 'minute')
    print(result2)
    
    result3 = convert_time(1, 'day', 'hour')
    print(result3)