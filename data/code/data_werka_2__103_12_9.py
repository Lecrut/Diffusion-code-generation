from datetime import time, timedelta

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def compute_elapsed_time_components(reference_time: time) -> tuple:
    midnight = time(0, 0, 0)
    delta = timedelta(hours=reference_time.hour, minutes=reference_time.minute, seconds=reference_time.second)
    total_seconds = int(delta.total_seconds())
    hours = total_seconds // SECONDS_PER_HOUR
    remainder = total_seconds % SECONDS_PER_HOUR
    minutes = remainder // SECONDS_PER_MINUTE
    seconds = remainder % SECONDS_PER_MINUTE
    return (hours, minutes, seconds)

if __name__ == '__main__':
    sample_time = time(10, 15, 30)
    hours, minutes, seconds = compute_elapsed_time_components(sample_time)
    print(f"{hours} hours, {minutes} minutes, {seconds} seconds")