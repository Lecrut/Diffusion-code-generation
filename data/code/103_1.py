import datetime
import pytz
def calculate_seconds_today():
    today = datetime.datetime.now(pytz.utc)
    start_of_day = today.replace(hour=0, minute=0, second=0, microsecond=0)
    time_passed = today - start_of_day
    return time_passed.total_seconds()
if __name__ == '__main__':
    seconds = calculate_seconds_today()
    print(seconds)