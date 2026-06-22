def convert_seconds_to_dhms(seconds):
    if not isinstance(seconds, int) or seconds < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    SECONDS_IN_DAY = 86400
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_MINUTE = 60
    
    days = seconds // SECONDS_IN_DAY
    remaining_seconds = seconds % SECONDS_IN_DAY
    hours = remaining_seconds // SECONDS_IN_HOUR
    remaining_seconds %= SECONDS_IN_HOUR
    minutes = remaining_seconds // SECONDS_IN_MINUTE
    remaining_seconds %= SECONDS_IN_MINUTE
    
    return days, hours, minutes, remaining_seconds

if __name__ == '__main__':
    sample_values = [86401, 90062, 3662, 7201, 123457, 0]
    for value in sample_values:
        try:
            print(convert_seconds_to_dhms(value))
        except ValueError as e:
            print(e)