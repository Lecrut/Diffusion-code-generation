import datetime
import pytz
def calculate_seconds_today():
    today = datetime.datetime.now(pytz.utc)
    start_of_day = today.replace(hour=0, minute=0, second=0, microsecond=0)
    time_difference = today - start_of_day
    return time_difference.total_seconds()
if __name__ == '__main__':
    total_seconds = calculate_seconds_today()
    print(total_seconds)