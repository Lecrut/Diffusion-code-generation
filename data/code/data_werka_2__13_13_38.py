def validate_input(total_seconds):
    if not isinstance(total_seconds, int) or total_seconds < 0:
        raise ValueError("Input must be a non-negative integer.")

def convert_seconds_to_dhms(total_seconds):
    validate_input(total_seconds)
    
    SECONDS_PER_DAY = 3600 * 24
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60
    
    days = total_seconds // SECONDS_PER_DAY
    hours = (total_seconds % SECONDS_PER_DAY) // SECONDS_PER_HOUR
    minutes = (total_seconds % SECONDS_PER_HOUR) // SECONDS_PER_MINUTE
    seconds = total_seconds % SECONDS_PER_MINUTE
    
    return days, hours, minutes, seconds

if __name__ == '__main__':
    sample_duration = 1234567
    days, hours, minutes, seconds = convert_seconds_to_dhms(sample_duration)
    print(f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds")