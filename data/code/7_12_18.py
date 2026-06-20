def convert_time(value, from_unit, to_unit):
    unit_to_seconds = {
        'ns': 1e-9,
        'us': 1e-6,
        'ms': 0.001,
        's': 1,
        'min': 60,
        'h': 3600,
        'd': 86400,
        'wk': 604800,
        'mo': 2629746,
        'y': 31556952,
        'sec': 1,
        'minute': 60,
        'hour': 3600,
        'day': 86400,
        'week': 604800,
        'month': 2629746,
        'year': 31556952
    }
    
    normalized_from = from_unit.lower()
    normalized_to = to_unit.lower()
    
    if normalized_from not in unit_to_seconds:
        raise ValueError(f"Unsupported from_unit: {from_unit}")
    if normalized_to not in unit_to_seconds:
        raise ValueError(f"Unsupported to_unit: {to_unit}")
    
    seconds = value * unit_to_seconds[normalized_from]
    result = seconds / unit_to_seconds[normalized_to]
    return result

if __name__ == '__main__':
    print(convert_time(1, 'h', 's'))
    print(convert_time(60, 'min', 's'))
    print(convert_time(24, 'h', 'd'))
    print(convert_time(1, 'd', 'h'))
    print(convert_time(1000, 'ms', 's'))