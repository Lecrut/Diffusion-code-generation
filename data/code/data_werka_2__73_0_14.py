import datetime
import pytz
from collections import namedtuple

TimeDeltaDetails = namedtuple("TimeDeltaDetails", ["total_seconds", "days", "hours", "minutes", "seconds"])

ZONE_MAP = {
    "UTC": pytz.utc,
    "EST": pytz.timezone("America/New_York"),
    "GMT": pytz.timezone("Europe/London"),
    "JST": pytz.timezone("Asia/Tokyo"),
}

def compute_tz_aware_delta(dt_start, dt_end):
    if dt_start.tzinfo is None:
        raise ValueError("Start datetime must be timezone-aware")
    if dt_end.tzinfo is None:
        raise ValueError("End datetime must be timezone-aware")
    
    start_utc = dt_start.astimezone(pytz.utc)
    end_utc = dt_end.astimezone(pytz.utc)
    
    delta = end_utc - start_utc
    total_secs = int(delta.total_seconds())
    
    days = total_secs // 86400
    rem = total_secs % 86400
    hours = rem // 3600
    rem = rem % 3600
    minutes = rem // 60
    seconds = rem % 60
    
    return TimeDeltaDetails(
        total_seconds=total_secs,
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds
    )

def main():
    tz_london = ZONE_MAP["GMT"]
    tz_new_york = ZONE_MAP["EST"]
    
    dt_london = datetime.datetime(2023, 10, 26, 10, 0, 0, tzinfo=tz_london)
    dt_new_york = datetime.datetime(2023, 10, 26, 5, 0, 0, tzinfo=tz_new_york)
    
    try:
        details = compute_tz_aware_delta(dt_london, dt_new_york)
        print(f"Datetime 1 (London): {dt_london}")
        print(f"Datetime 2 (New York): {dt_new_york}")
        print(f"Delta Details: {details}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()