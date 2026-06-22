from datetime import time

SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600

def compute_elapsed_time_components(current_time: time):
    if not isinstance(current_time, time):
        raise TypeError("current_time must be a datetime.time instance")
    
    midnight = time(0, 0, 0)
    
    if current_time < midnight:
        raise ValueError("Time must be today or later")
    
    total_seconds = current_time.hour * SECONDS_PER_HOUR + \
                    current_time.minute * SECONDS_PER_MINUTE + \
                    current_time.second
    
    hours = total_seconds // SECONDS_PER_HOUR
    remaining_seconds = total_seconds % SECONDS_PER_HOUR
    minutes = remaining_seconds // SECONDS_PER_MINUTE
    seconds = remaining_seconds % SECONDS_PER_MINUTE
    
    return hours, minutes, seconds

if __name__ == '__main__':
    from datetime import time as dt_time
    sample_time = dt_time(14, 30, 45)
    hours, minutes, seconds = compute_elapsed_time_components(sample_time)
    print(f"{hours} hours, {minutes} minutes, {seconds} seconds")