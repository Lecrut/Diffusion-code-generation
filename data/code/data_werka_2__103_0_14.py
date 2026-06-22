import datetime

def compute_seconds_since_midnight():
    current_time = datetime.datetime.now()
    start_of_day = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
    time_difference = current_time - start_of_day
    elapsed_seconds = time_difference.total_seconds()
    return elapsed_seconds

if __name__ == '__main__':
    sample_seconds = compute_seconds_since_midnight()
    print(sample_seconds)