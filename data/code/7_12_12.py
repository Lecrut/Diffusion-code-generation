def convert_time(value, from_unit, to_unit):
    units = {
        'nanosecond': 1e-9,
        'ns': 1e-9,
        'microsecond': 1e-6,
        'us': 1e-6,
        'millisecond': 1e-3,
        'ms': 1e-3,
        'second': 1,
        's': 1,
        'minute': 60,
        'min': 60,
        'hour': 3600,
        'h': 3600,
        'day': 86400,
        'd': 86400,
        'week': 604800,
        'wk': 604800,
        'month': 2629800,
        'mo': 2629800,
        'year': 31557600,
        'yr': 31557600
    }
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit not in units:
        raise ValueError(f"Invalid from_unit: {from_unit}")
    if to_unit not in units:
        raise ValueError(f"Invalid to_unit: {to_unit}")
    seconds = value * units[from_unit]
    result = seconds / units[to_unit]
    return result

if __name__ == '__main__':
    val1 = 60
    res1 = convert_time(val1, 'minute', 'second')
    print(res1)
    val2 = 1000
    res2 = convert_time(val2, 'millisecond', 'second')
    print(res2)
    val3 = 1
    res3 = convert_time(val3, 'hour', 'minute')
    print(res3)
    val4 = 1
    res4 = convert_time(val4, 'day', 'hour')
    print(res4)
    val5 = 1
    res5 = convert_time(val5, 'year', 'day')
    print(res5)