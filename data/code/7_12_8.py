def convert_time(value, from_unit, to_unit):
    units_to_seconds = {
        'ns': 1e-9,
        'us': 1e-6,
        'ms': 1e-3,
        's': 1.0,
        'min': 60.0,
        'h': 3600.0,
        'd': 86400.0,
        'wk': 604800.0,
    }
    
    if from_unit not in units_to_seconds:
        raise ValueError(f"Unknown from_unit: {from_unit}")
    if to_unit not in units_to_seconds:
        raise ValueError(f"Unknown to_unit: {to_unit}")
        
    seconds = value * units_to_seconds[from_unit]
    result = seconds / units_to_seconds[to_unit]
    
    if result == int(result):
        return int(result)
    return result

if __name__ == '__main__':
    result = convert_time(1.5, 'h', 'min')
    print(result)
    
    result2 = convert_time(3600, 's', 'h')
    print(result2)
    
    result3 = convert_time(1, 'd', 's')
    print(result3)