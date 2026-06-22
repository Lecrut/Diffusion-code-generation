from datetime import datetime, timedelta

def get_elapsed_since_midnight():
    now = datetime.now()
    start_of_day = datetime.min.replace(year=now.year, month=now.month, day=now.day)
    elapsed = now - start_of_day
    total_seconds = int(elapsed.total_seconds())
    hours = total_seconds // 3600
    remaining = total_seconds % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    return timedelta(hours=hours, minutes=minutes, seconds=seconds)

if __name__ == '__main__':
    result = get_elapsed_since_midnight()
    print(result)