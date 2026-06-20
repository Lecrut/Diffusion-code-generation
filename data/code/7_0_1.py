def convert_time(value, source_unit, target_unit):
    units_to_seconds = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600
    }

    if source_unit not in units_to_seconds or target_unit not in units_to_seconds:
        raise ValueError("Invalid unit. Use 'seconds', 'minutes', or 'hours'.")

    if value < 0:
        raise ValueError("Time value cannot be negative.")

    seconds = value * units_to_seconds[source_unit]
    result = seconds / units_to_seconds[target_unit]

    return result

if __name__ == '__main__':
    result1 = convert_time(1, 'hours', 'minutes')
    print(result1)

    result2 = convert_time(90, 'minutes', 'seconds')
    print(result2)

    result3 = convert_time(3600, 'seconds', 'hours')
    print(result3)