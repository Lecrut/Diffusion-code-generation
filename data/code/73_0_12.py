import pytz
from datetime import datetime, timedelta

def calculate_time_difference(dt1, dt2):
    if dt1.tzinfo is None:
        dt1 = pytz.utc.localize(dt1)
    if dt2.tzinfo is None:
        dt2 = pytz.utc.localize(dt2)
    diff = dt2 - dt1
    total_seconds = int(diff.total_seconds())
    sign = 1 if total_seconds >= 0 else -1
    abs_seconds = abs(total_seconds)
    days = abs_seconds // 86400
    remaining_seconds = abs_seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds = remaining_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

if __name__ == '__main__':
    tz_london = pytz.timezone('Europe/London')
    tz_new_york = pytz.timezone('America/New_York')
    dt1 = datetime(2023, 10, 1, 12, 0, 0)
    dt2 = datetime(2023, 10, 1, 12, 0, 0)
    dt1_aware = tz_london.localize(dt1)
    dt2_aware = tz_new_york.localize(dt2)
    result = calculate_time_difference(dt1_aware, dt2_aware)
    print(result)