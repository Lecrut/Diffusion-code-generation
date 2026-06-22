import datetime

SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

def calculate_seconds_since_midnight():
    now = datetime.datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - midnight
    return delta.total_seconds()

def validate_seconds_input(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be numeric")
    if value < 0:
        raise ValueError("Value must be non-negative")
    if value >= SECONDS_IN_DAY:
        raise ValueError("Value must be less than a full day")
    return True

def format_elapsed_time(total_seconds):
    validate_seconds_input(total_seconds)
    hours = int(total_seconds // SECONDS_IN_HOUR)
    remaining_seconds = total_seconds - (hours * SECONDS_IN_HOUR)
    minutes = int(remaining_seconds // SECONDS_IN_MINUTE)
    seconds = remaining_seconds - (minutes * SECONDS_IN_MINUTE)
    return (hours, minutes, seconds)

if __name__ == '__main__':
    current_seconds = calculate_seconds_since_midnight()
    print(current_seconds)
    
    sample_seconds = 3661
    hours, minutes, seconds = format_elapsed_time(sample_seconds)
    print(f"{hours}:{minutes}:{seconds}")