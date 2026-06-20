def convert_time(value, source_unit, target_unit):
    units = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600
    }
    if source_unit not in units or target_unit not in units:
        raise ValueError("Invalid unit. Use 'seconds', 'minutes', or 'hours'.")
    if value < 0:
        raise ValueError("Time value cannot be negative.")
    value_in_seconds = value * units[source_unit]
    result = value_in_seconds / units[target_unit]
    return result

if __name__ == '__main__':
    print(convert_time(1, 'hours', 'minutes'))
    print(convert_time(90, 'minutes', 'seconds'))
    print(convert_time(3600, 'seconds', 'hours'))
    print(convert_time(2.5, 'hours', 'seconds'))