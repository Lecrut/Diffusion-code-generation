import pytz
from datetime import datetime

def calculate_time_difference(dt1, dt2):
    if dt1.tzinfo is None:
        dt1 = pytz.utc.localize(dt1)
    if dt2.tzinfo is None:
        dt2 = pytz.utc.localize(dt2)
    else:
        dt1 = dt1.astimezone(pytz.utc)
        dt2 = dt2.astimezone(pytz.utc)
    delta = dt2 - dt1
    return delta

if __name__ == '__main__':
    tz_ny = pytz.timezone('America/New_York')
    tz_tokyo = pytz.timezone('Asia/Tokyo')
    dt1 = datetime(2023, 10, 1, 12, 0, 0)
    dt2 = datetime(2023, 10, 1, 12, 0, 0)
    dt1_aware = tz_ny.localize(dt1)
    dt2_aware = tz_tokyo.localize(dt2)
    result = calculate_time_difference(dt1_aware, dt2_aware)
    print(result)