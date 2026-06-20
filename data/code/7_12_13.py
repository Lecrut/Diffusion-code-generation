def convert_time(value, from_unit, to_unit):
    unit_to_seconds = {
        'nanosecond': 1e-9,
        'microsecond': 1e-6,
        'millisecond': 1e-3,
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
    if from_unit_lower not in unit_to_seconds:
        raise ValueError(f"Unknown time unit: {from_unit}")
    if to_unit_lower not in unit_to_seconds:
        raise ValueError(f"Unknown time unit: {to_unit}")
    value_in_seconds = value * unit_to_seconds[from_unit_lower]
    result = value_in_seconds / unit_to_seconds[to_unit_lower]
    return result

if __name__ == '__main__':
    print(convert_time(1, 'hour', 'minute'))
    print(convert_time(5, 'day', 'second'))
    print(convert_time(1000, 'millisecond', 'second'))
    print(convert_time(2, 'year', 'month'))