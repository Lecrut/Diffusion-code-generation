from datetime import time, timedelta

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def compute_elapsed_time_components(current_time: time) -> tuple:
    midnight = time(0, 0, 0)
    delta = timedelta(
        hours=current_time.hour,
        minutes=current_time.minute,
        seconds=current_time.second,
    )
    total_seconds = int(delta.total_seconds())
    hours = total_seconds // SECONDS_PER_HOUR
    remainder_after_hours = total_seconds % SECONDS_PER_HOUR
    minutes = remainder_after_hours // SECONDS_PER_MINUTE
    seconds = remainder_after_hours % SECONDS_PER_MINUTE
    return (hours, minutes, seconds)

if __name__ == '__main__':
    sample_time = time(10, 15, 30)
    h, m, s = compute_elapsed_time_components(sample_time)
    print(f"{h} hours, {m} minutes, {s} seconds")