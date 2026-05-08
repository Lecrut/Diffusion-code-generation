import datetime
import pytz
def calculate_seconds_today():
    now = datetime.datetime.now(pytz.utc)
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - start_of_day
    return delta.total_seconds()
if __name__ == '__main__':
    total_seconds = calculate_seconds_today()
    print(total_seconds)