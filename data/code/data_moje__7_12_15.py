def convert_time(value, from_unit, to_unit):
    units = {
        'ns': 1e-9,
        'us': 1e-6,
        'µs': 1e-6,
        'ms': 1e-3,
        's': 1,
        'sec': 1,
        'min': 60,
        'h': 3600,
        'hr': 3600,
        'day': 86400,
        'wk': 604800,
        'week': 604800,
        'mo': 2629746,
        'month': 2629746,
        'y': 31556952,
        'yr': 31556952,
        'year': 31556952
    }
    
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit not in units:
        raise ValueError(f"Unsupported from_unit: {from_unit}")
    if to_unit not in units:
        raise ValueError(f"Unsupported to_unit: {to_unit}")
    
    seconds = value * units[from_unit]
    result = seconds / units[to_unit]
    
    return result

if __name__ == '__main__':
    sample_value = 60
    sample_from = 'min'
    sample_to = 's'
    converted = convert_time(sample_value, sample_from, sample_to)
    print(converted)
    
    sample_value2 = 1000
    sample_from2 = 'ms'
    sample_to2 = 's'
    converted2 = convert_time(sample_value2, sample_from2, sample_to2)
    print(converted2)
    
    sample_value3 = 1
    sample_from3 = 'wk'
    sample_to3 = 'day'
    converted3 = convert_time(sample_value3, sample_from3, sample_to3)
    print(converted3)
    
    sample_value4 = 31556952
    sample_from4 = 's'
    sample_to4 = 'year'
    converted4 = convert_time(sample_value4, sample_from4, sample_to4)
    print(converted4)