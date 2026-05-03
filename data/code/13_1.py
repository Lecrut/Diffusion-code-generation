from datetime import datetime
from datetime import timedelta
import pytz
def calculate_time_delta(dt1: datetime, dt2: datetime) -> timedelta:
    if dt1.tzinfo is None or dt2.tzinfo is None:
        raise ValueError("Both datetime objects must be timezone-aware")
    return dt2 - dt1
if __name__ == '__main__':
    tz_london = pytz.timezone('Europe/London')
    tz_new_york = pytz.timezone('America/New_York')
    dt_london_start = datetime(2023, 10, 26, 10, 0, 0, tzinfo=tz_london)
    dt_london_end = datetime(2023, 10, 26, 12, 30, 0, tzinfo=tz_london)
    dt_ny_start = datetime(2023, 10, 26, 14, 0, 0, tzinfo=tz_new_york)
    dt_ny_end = datetime(2023, 10, 26, 16, 0, 0, tzinfo=tz_new_york)
    delta1 = calculate_time_delta(dt_london_start, dt_london_end)
    print(f"Delta 1: {delta1}")
    delta2 = calculate_time_delta(dt_ny_start, dt_ny_end)
    print(f"Delta 2: {delta2}")