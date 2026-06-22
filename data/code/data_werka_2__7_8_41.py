def convert_time(duration, unit):
    SECONDS_IN_MINUTE = 60
    MINUTES_IN_HOUR = 60
    HOURS_IN_DAY = 24

    if not isinstance(duration, (int, float)):
        raise ValueError("Duration must be a number.")
    
    if duration < 0:
        raise ValueError("Duration cannot be negative.")

    supported_units = {
        'seconds': 1,
        'minutes': SECONDS_IN_MINUTE,
        'hours': MINUTES_IN_HOUR * SECONDS_IN_MINUTE,
        'days': HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE
    }

    if unit not in supported_units:
        raise ValueError(f"Unsupported unit: {unit}")

    total_seconds = duration * supported_units[unit]
    
    return {
        'seconds': total_seconds,
        'minutes': total_seconds / SECONDS_IN_MINUTE,
        'hours': total_seconds / (SECONDS_IN_MINUTE * MINUTES_IN_HOUR),
        'days': total_seconds / (SECONDS_IN_MINUTE * MINUTES_IN_HOUR * HOURS_IN_DAY)
    }

if __name__ == '__main__':
    try:
        sample_duration = 48
        sample_unit = 'hours'
        converted_times = convert_time(sample_duration, sample_unit)
        print(converted_times)
    except ValueError as e:
        print(e)