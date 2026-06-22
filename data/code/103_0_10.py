import datetime

def compute_seconds_since_midnight():
    current_time = datetime.datetime.now()
    midnight_today = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
    time_difference = current_time - midnight_today
    seconds_elapsed = time_difference.total_seconds()
    return seconds_elapsed

if __name__ == '__main__':
    sample_seconds = compute_seconds_since_midnight()
    print(sample_seconds)