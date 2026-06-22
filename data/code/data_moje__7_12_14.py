def convert_time(value, from_unit, to_unit):
    if value == 0:
        return 0.0
    
    base_conversion_factors = {
        'ns': 1e-9,
        'us': 1e-6,
        'ms': 1e-3,
        's': 1.0,
        'min': 60.0,
        'h': 3600.0,
        'd': 86400.0,
        'w': 604800.0,
        'mo': 2629746.0,
        'y': 31556952.0
    }
    
    from_val = value * base_conversion_factors[from_unit]
    result = from_val / base_conversion_factors[to_unit]
    
    return result

if __name__ == '__main__':
    result = convert_time(1, 'h', 'min')
    print(result)