import time

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def get_elapsed_time_since_midnight():
    current_timestamp = time.time()
    seconds_into_day = current_timestamp % SECONDS_PER_HOUR
    total_seconds = int(seconds_into_day)
    hours = total_seconds // SECONDS_PER_HOUR
    remaining_after_hours = total_seconds % SECONDS_PER_HOUR
    minutes = remaining_after_hours // SECONDS_PER_MINUTE
    seconds = remaining_after_hours % SECONDS_PER_MINUTE
    if not isinstance(hours, int) or not isinstance(minutes, int) or not isinstance(seconds, int):
        raise ValueError("Calculated time components must be integers")
    return (hours, minutes, seconds)

if __name__ == '__main__':
    elapsed = get_elapsed_time_since_midnight()
    print(elapsed)