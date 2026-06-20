def convert_time(value, from_unit, to_unit):
    unit_to_seconds = {
        'second': 1,
        'minute': 60,
        'hour': 3600,
        'day': 86400,
        'month': 86400 * 30.44,
        'year': 86400 * 365.25
    }
    if from_unit not in unit_to_seconds:
        raise ValueError(f"Unsupported unit: {from_unit}")
    if to_unit not in unit_to_seconds:
        raise ValueError(f"Unsupported unit: {to_unit}")
    
    value_in_seconds = value * unit_to_seconds[from_unit]
    result = value_in_seconds / unit_to_seconds[to_unit]
    return result

if __name__ == '__main__':
    print(convert_time(1, 'year', 'day'))
    print(convert_time(24, 'hour', 'minute'))
    print(convert_time(1, 'month', 'hour'))
    print(convert_time(365.25, 'day', 'year'))
    print(convert_time(90, 'day', 'month'))