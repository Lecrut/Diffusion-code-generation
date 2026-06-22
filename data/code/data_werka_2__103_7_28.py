import datetime

def get_seconds_since_midnight():
    now = datetime.datetime.now()
    start_of_day = datetime.datetime.min.replace(year=now.year, month=now.month, day=now.day)
    delta = now - start_of_day
    total_seconds = delta.total_seconds()
    if total_seconds < 0:
        raise ValueError("Elapsed time cannot be negative")
    return total_seconds

if __name__ == '__main__':
    elapsed_seconds = get_seconds_since_midnight()
    print(elapsed_seconds)