def convert_time(value, from_unit, to_unit):
    base_unit = 's'
    factors = {
        'ns': 1e-9,
        'us': 1e-6,
        'µs': 1e-6,
        'ms': 1e-3,
        's': 1.0,
        'min': 60.0,
        'h': 3600.0,
        'd': 86400.0,
        'wk': 604800.0,
        'mo': 2629746.0,
        'y': 31556952.0
    }
    
    if from_unit not in factors:
        raise ValueError(f"Unsupported unit: {from_unit}")
    if to_unit not in factors:
        raise ValueError(f"Unsupported unit: {to_unit}")
    
    value_in_seconds = value * factors[from_unit]
    result = value_in_seconds / factors[to_unit]
    return result

if __name__ == '__main__':
    result1 = convert_time(60, 'min', 's')
    print(result1)
    result2 = convert_time(1.5, 'h', 'min')
    print(result2)
    result3 = convert_time(1000, 'ms', 's')
    print(result3)
    result4 = convert_time(365, 'd', 'h')
    print(result4)