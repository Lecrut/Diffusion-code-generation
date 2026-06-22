def convert_time(value, from_unit, to_unit):
    unit_to_seconds = {
        'ns': 1e-9,
        'us': 1e-6,
        'ms': 1e-3,
        's': 1,
        'min': 60,
        'h': 3600,
        'day': 86400,
        'week': 604800,
        'month': 2629746,
        'year': 31556952
    }
    
    if from_unit not in unit_to_seconds or to_unit not in unit_to_seconds:
        raise ValueError(f"Unsupported time unit: {from_unit if from_unit not in unit_to_seconds else to_unit}")
    
    value_in_seconds = value * unit_to_seconds[from_unit]
    result = value_in_seconds / unit_to_seconds[to_unit]
    
    return result

if __name__ == '__main__':
    result = convert_time(1, 'h', 'min')
    print(result)
    
    result2 = convert_time(3600, 's', 'h')
    print(result2)
    
    result3 = convert_time(1, 'day', 'h')
    print(result3)