def convert_time(time_value, source_unit, target_unit):
    units_to_seconds = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600
    }

    if source_unit not in units_to_seconds or target_unit not in units_to_seconds:
        raise ValueError("Invalid unit. Use 'seconds', 'minutes', or 'hours'.")

    if time_value < 0:
        raise ValueError("Time value cannot be negative.")

    seconds = time_value * units_to_seconds[source_unit]
    converted_value = seconds / units_to_seconds[target_unit]

    return converted_value

if __name__ == '__main__':
    print(convert_time(90, 'minutes', 'hours'))
    print(convert_time(3600, 'seconds', 'minutes'))
    print(convert_time(2.5, 'hours', 'seconds'))
    print(convert_time(1500, 'seconds', 'hours'))