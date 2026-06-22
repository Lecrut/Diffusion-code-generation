import pytz
from datetime import datetime

def calculate_time_difference(start_dt, end_dt):
    if start_dt.tzinfo is None:
        start_dt = pytz.utc.localize(start_dt)
    if end_dt.tzinfo is None:
        end_dt = pytz.utc.localize(end_dt)
    start_utc = start_dt.astimezone(pytz.utc)
    end_utc = end_dt.astimezone(pytz.utc)
    delta = end_utc - start_utc
    return delta

if __name__ == '__main__':
    tz_ny = pytz.timezone('America/New_York')
    tz_london = pytz.timezone('Europe/London')
    start_naive = datetime(2023, 10, 1, 12, 0, 0)
    end_naive = datetime(2023, 10, 1, 18, 0, 0)
    start_ny = tz_ny.localize(start_naive)
    end_london = tz_london.localize(end_naive)
    result = calculate_time_difference(start_ny, end_london)
    print(result)