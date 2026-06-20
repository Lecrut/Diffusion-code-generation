def convert_time(value, from_unit, to_unit):
    units = {
        'ns': 1e-9,
        'us': 1e-6,
        'ms': 1e-3,
        's': 1,
        'min': 60,
        'h': 3600,
        'd': 86400,
        'wk': 604800,
        'mo': 2629800,
        'y': 31557600
    }
    
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    
    if from_unit_lower not in units or to_unit_lower not in units:
        raise ValueError(f"Invalid time unit: {from_unit if from_unit_lower not in units else to_unit}")
    
    seconds = value * units[from_unit_lower]
    result = seconds / units[to_unit_lower]
    return result

if __name__ == '__main__':
    result1 = convert_time(60, 'min', 's')
    print(result1)
    result2 = convert_time(1000, 'ms', 's')
    print(result2)
    result3 = convert_time(2, 'h', 'min')
    print(result3)
    result4 = convert_time(1, 'y', 'mo')
    print(result4)
    result5 = convert_time(3600, 's', 'h')
    print(result5)