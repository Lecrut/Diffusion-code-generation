import time

def calculate_elapsed_since_midnight():
    current_time = time.time()
    seconds_in_day = 86400
    start_of_day_timestamp = current_time - (current_time % seconds_in_day)
    elapsed_seconds = current_time - start_of_day_timestamp
    if not isinstance(elapsed_seconds, (int, float)):
        raise ValueError("Elapsed time must be numeric")
    total_hours = int(elapsed_seconds // 3600)
    remaining_seconds = elapsed_seconds - (total_hours * 3600)
    total_minutes = int(remaining_seconds // 60)
    total_seconds = remaining_seconds - (total_minutes * 60)
    if total_hours < 0 or total_minutes < 0 or total_seconds < 0:
        raise ValueError("Time components cannot be negative")
    return (total_hours, total_minutes, total_seconds)

if __name__ == '__main__':
    elapsed_time = calculate_elapsed_since_midnight()
    print(elapsed_time)