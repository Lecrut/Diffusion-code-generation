import datetime

def compute_seconds_since_midnight():
    current_time = datetime.datetime.now()
    start_of_day = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed = current_time - start_of_day
    return elapsed.total_seconds()

if __name__ == '__main__':
    seconds = compute_seconds_since_midnight()
    print(seconds)