import pytz
from datetime import datetime, timedelta

def calculate_time_difference(start_dt, end_dt):
    if start_dt.tzinfo is None:
        start_dt = pytz.utc.localize(start_dt)
    if end_dt.tzinfo is None:
        end_dt = pytz.utc.localize(end_dt)
    else:
        start_dt = start_dt.astimezone(pytz.utc)
        end_dt = end_dt.astimezone(pytz.utc)
    delta = end_dt - start_dt
    total_seconds = int(delta.total_seconds())
    days = total_seconds // 86400
    remainder = total_seconds % 86400
    hours = remainder // 3600
    remainder = remainder % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    return {
        'total_seconds': total_seconds,
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds
    }

if __name__ == '__main__':
    tz_ny = pytz.timezone('US/Eastern')
    tz_london = pytz.timezone('Europe/London')
    start_dt = tz_ny.localize(datetime(2023, 10, 1, 12, 0, 0))
    end_dt = tz_london.localize(datetime(2023, 10, 1, 18, 0, 0))
    result = calculate_time_difference(start_dt, end_dt)
    print(result)