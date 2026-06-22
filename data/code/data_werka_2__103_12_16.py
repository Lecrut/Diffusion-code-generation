from datetime import time

def get_elapsed_time(current_time: time) -> tuple:
    if current_time is None:
        raise ValueError("Time cannot be None")
    midnight = time(0, 0, 0)
    if current_time < midnight:
        raise ValueError("Time cannot be before midnight")
    total_seconds = current_time.hour * 3600 + current_time.minute * 60 + current_time.second
    hours = total_seconds // 3600
    remaining = total_seconds % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    return hours, minutes, seconds

if __name__ == '__main__':
    sample_time = time(14, 30, 45)
    hours, minutes, seconds = get_elapsed_time(sample_time)
    print(f"{hours} hours, {minutes} minutes, {seconds} seconds")