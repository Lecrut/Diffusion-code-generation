from datetime import datetime

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def compute_time_delta_in_parts(start_time: datetime, end_time: datetime) -> tuple:
    delta = end_time - start_time
    total_seconds = int(delta.total_seconds())
    
    is_negative = total_seconds < 0
    absolute_seconds = abs(total_seconds)
    
    hours = absolute_seconds // SECONDS_PER_HOUR
    remainder_after_hours = absolute_seconds % SECONDS_PER_HOUR
    
    minutes = remainder_after_hours // SECONDS_PER_MINUTE
    seconds = remainder_after_hours % SECONDS_PER_MINUTE
    
    if is_negative:
        return (-hours, -minutes, -seconds)
    else:
        return (hours, minutes, seconds)

if __name__ == '__main__':
    t1 = datetime(2023, 10, 1, 10, 30, 0)
    t2 = datetime(2023, 10, 1, 14, 45, 30)
    
    result = compute_time_delta_in_parts(t1, t2)
    print(result)