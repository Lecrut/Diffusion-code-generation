def validate_input(total_seconds):
    if not isinstance(total_seconds, int) or total_seconds < 0:
        raise ValueError("Input must be a non-negative integer.")

def convert_seconds_to_dhms(total_seconds):
    validate_input(total_seconds)
    
    SECONDS_IN_DAY = 3600 * 24
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_MINUTE = 60
    
    days = total_seconds // SECONDS_IN_DAY
    hours = (total_seconds % SECONDS_IN_DAY) // SECONDS_IN_HOUR
    minutes = (total_seconds % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
    seconds = total_seconds % SECONDS_IN_MINUTE
    
    return days, hours, minutes, seconds

if __name__ == '__main__':
    sample_duration = 1234567
    days, hours, minutes, seconds = convert_seconds_to_dhms(sample_duration)
    print(f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds")