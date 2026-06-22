def convert_time(value, from_unit, to_unit):
    conversion_to_seconds = {
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
    if from_unit_lower not in conversion_to_seconds:
        raise ValueError(f"Invalid from_unit: {from_unit}")
    if to_unit_lower not in conversion_to_seconds:
        raise ValueError(f"Invalid to_unit: {to_unit}")
    seconds = value * conversion_to_seconds[from_unit_lower]
    result = seconds / conversion_to_seconds[to_unit_lower]
    return result

if __name__ == '__main__':
    result1 = convert_time(1, 'hour', 'minute')
    print(result1)
    result2 = convert_time(2.5, 'day', 'second')
    print(result2)
    result3 = convert_time(1000, 'millisecond', 'nanosecond')
    print(result3)