def convert_time(value, source_unit, target_unit):
    units_in_seconds = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600
    }

    if source_unit not in units_in_seconds:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    if target_unit not in units_in_seconds:
        raise ValueError(f"Unsupported target unit: {target_unit}")

    seconds = value * units_in_seconds[source_unit]
    return seconds / units_in_seconds[target_unit]

if __name__ == '__main__':
    result = convert_time(7200, 'seconds', 'hours')
    print(result)