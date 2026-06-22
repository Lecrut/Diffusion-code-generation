def convert_time(value, source_unit, target_unit):
    if source_unit == target_unit:
        return value

    to_seconds = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600
    }

    if source_unit not in to_seconds or target_unit not in to_seconds:
        raise ValueError("Invalid unit. Use 'seconds', 'minutes', or 'hours'.")

    seconds = value * to_seconds[source_unit]
    return seconds / to_seconds[target_unit]

if __name__ == '__main__':
    print(convert_time(3600, 'seconds', 'hours'))
    print(convert_time(2.5, 'hours', 'minutes'))
    print(convert_time(90, 'minutes', 'seconds'))