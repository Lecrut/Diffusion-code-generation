import datetime
import time
def calculate_seconds_today():
    now = datetime.datetime.now(datetime.timezone.utc)
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - start_of_day
    return delta.total_seconds()
if __name__ == '__main__':
    seconds = calculate_seconds_today()
    print(seconds)