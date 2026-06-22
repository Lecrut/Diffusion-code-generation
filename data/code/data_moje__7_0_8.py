def convert_time(value, source_unit, target_unit):
    units = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'second': 1,
        'minute': 60,
        'hour': 3600
    }
    source_key = source_unit.lower()
    target_key = target_unit.lower()
    if source_key not in units:
        raise ValueError(f"Invalid source unit: {source_unit}")
    if target_key not in units:
        raise ValueError(f"Invalid target unit: {target_unit}")
    seconds = value * units[source_key]
    return seconds / units[target_key]

if __name__ == '__main__':
    result1 = convert_time(60, 'seconds', 'minutes')
    print(result1)
    result2 = convert_time(2, 'hours', 'minutes')
    print(result2)
    result3 = convert_time(180, 'minutes', 'hours')
    print(result3)
    result4 = convert_time(90, 'minutes', 'seconds')
    print(result4)
    result5 = convert_time(0.5, 'hours', 'seconds')
    print(result5)