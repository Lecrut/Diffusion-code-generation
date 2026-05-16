from datetime import datetime
from datetime import timedelta
import pytz
def calculate_time_delta(dt1: datetime, dt2: datetime) -> timedelta:
    if dt1.tzinfo is None or dt2.tzinfo is None:
        raise ValueError("Both datetime objects must be timezone-aware")
    return dt2 - dt1
if __name__ == '__main__':
    tz_utc = pytz.utc
    dt_utc1 = tz_utc.localize(datetime(2023, 1, 1, 10, 0, 0))
    dt_utc2 = tz_utc.localize(datetime(2023, 1, 3, 12, 30, 0))
    delta1 = calculate_time_delta(dt_utc1, dt_utc2)
    print(f"Delta 1: {delta1}")
    dt_london = pytz.timezone('Europe/London')
    dt_london1 = dt_london.localize(datetime(2023, 1, 1, 10, 0, 0))
    dt_london2 = dt_london.localize(datetime(2023, 1, 3, 12, 30, 0))
    delta2 = calculate_time_delta(dt_london1, dt_london2)
    print(f"Delta 2: {delta2}")