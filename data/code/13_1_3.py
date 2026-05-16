from datetime import datetime
from datetime import timedelta
import pytz
def calculate_time_delta(dt1: datetime, dt2: datetime) -> timedelta:
    if dt1.tzinfo is None or dt2.tzinfo is None:
        raise ValueError("Input datetime objects must be timezone-aware")
    return dt2 - dt1
if __name__ == '__main__':
    tz_ny = pytz.timezone('America/New_York')
    tz_london = pytz.timezone('Europe/London')
    dt_ny_start = datetime(2023, 10, 26, 10, 0, 0, tzinfo=tz_ny)
    dt_london_end = datetime(2023, 10, 26, 16, 0, 0, tzinfo=tz_london)
    delta = calculate_time_delta(dt_ny_start, dt_london_end)
    print(f"Start Time (NY): {dt_ny_start}")
    print(f"End Time (London): {dt_london_end}")
    print(f"Time Delta: {delta}")
    dt_london_start = datetime(2023, 10, 26, 16, 0, 0, tzinfo=tz_london)
    dt_ny_end = datetime(2023, 10, 26, 10, 0, 0, tzinfo=tz_ny)
    delta_reverse = calculate_time_delta(dt_london_start, dt_ny_end)
    print(f"\nStart Time (London): {dt_london_start}")
    print(f"End Time (NY): {dt_ny_end}")
    print(f"Time Delta (Reverse): {delta_reverse}")