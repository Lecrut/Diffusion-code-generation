import datetime

def get_elapsed_seconds_since_day_start():
    now = datetime.datetime.now()
    start_of_day = datetime.datetime.min.replace(year=now.year, month=now.month, day=now.day)
    delta = now - start_of_day
    total_seconds = delta.total_seconds()
    if total_seconds < 0:
        raise ValueError("Elapsed time cannot be negative")
    return total_seconds

if __name__ == '__main__':
    result = get_elapsed_seconds_since_day_start()
    print(result)