def convert_seconds_to_dhms(seconds):
    if not isinstance(seconds, int) or seconds < 0:
        raise ValueError("Input must be a non-negative integer")
    
    SECONDS_IN_DAY = 3600 * 24
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_MINUTE = 60
    
    days = seconds // SECONDS_IN_DAY
    remaining_seconds_after_days = seconds % SECONDS_IN_DAY
    
    hours = remaining_seconds_after_days // SECONDS_IN_HOUR
    remaining_seconds_after_hours = remaining_seconds_after_days % SECONDS_IN_HOUR
    
    minutes = remaining_seconds_after_hours // SECONDS_IN_MINUTE
    remaining_seconds = remaining_seconds_after_hours % SECONDS_IN_MINUTE
    
    return days, hours, minutes, remaining_seconds

if __name__ == '__main__':
    sample_values = [100000, 43200, 987654, 6000, 3600, 60, 0]
    for value in sample_values:
        print(convert_seconds_to_dhms(value))