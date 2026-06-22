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
        'month': 2629746,
        'year': 31556952
    }
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    if from_unit_lower not in unit_to_seconds:
        raise ValueError(f"Unsupported from_unit: {from_unit}")
    if to_unit_lower not in unit_to_seconds:
        raise ValueError(f"Unsupported to_unit: {to_unit}")
    seconds = value * unit_to_seconds[from_unit_lower]
    result = seconds / unit_to_seconds[to_unit_lower]
    return result

if __name__ == '__main__':
    print(convert_time(1, 'hour', 'minute'))
    print(convert_time(90, 'minute', 'second'))
    print(convert_time(2, 'day', 'hour'))
    print(convert_time(1, 'year', 'day'))
    print(convert_time(500, 'millisecond', 'second'))
    print(convert_time(0.5, 'hour', 'minute'))