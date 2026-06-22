from datetime import time

def calculate_elapsed_time_since_midnight(current_time: time) -> dict:
    if not isinstance(current_time, time):
        raise TypeError("Input must be a datetime.time object")

    midnight = time(0, 0, 0)
    
    if current_time < midnight:
        raise ValueError("Time cannot be before midnight")

    hours = current_time.hour
    minutes = current_time.minute
    seconds = current_time.second
    
    return {
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }

if __name__ == '__main__':
    from datetime import time as dt_time
    sample_time = dt_time(14, 30, 45)
    result = calculate_elapsed_time_since_midnight(sample_time)
    print(result)