import time

def validate_input():
    current_time = time.time()
    if not isinstance(current_time, (int, float)) or current_time < 0:
        raise ValueError("Current time must be a non-negative number")

def elapsed_time_since_midnight():
    validate_input()
    start_of_day_timestamp = time.mktime((time.localtime().tm_year,
                                          time.localtime().tm_mon,
                                          time.localtime().tm_mday, 0, 0, 0, 0, 0, -1))
    current_time = time.time()
    elapsed_seconds = int(current_time - start_of_day_timestamp)
    hours = elapsed_seconds // 3600
    minutes = (elapsed_seconds % 3600) // 60
    seconds = elapsed_seconds % 60
    return f"{hours} hours, {minutes} minutes, and {seconds} seconds"

if __name__ == '__main__':
    print(elapsed_time_since_midnight())