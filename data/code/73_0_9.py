import datetime
import pytz

def compute_delta_seconds(dt_start, dt_end):
    if dt_start.tzinfo is None:
        raise ValueError("dt_start must be timezone-aware")
    if dt_end.tzinfo is None:
        raise ValueError("dt_end must be timezone-aware")
    utc = pytz.utc
    start_utc = dt_start.astimezone(utc)
    end_utc = dt_end.astimezone(utc)
    delta = end_utc - start_utc
    total_seconds = delta.total_seconds()
    return total_seconds

if __name__ == '__main__':
    tz_tokyo = pytz.timezone('Asia/Tokyo')
    tz_pacific = pytz.timezone('America/Los_Angeles')
    event_tokyo = datetime.datetime(2023, 12, 1, 12, 0, 0, tzinfo=tz_tokyo)
    event_pacific = datetime.datetime(2023, 12, 1, 12, 0, 0, tzinfo=tz_pacific)
    result = compute_delta_seconds(event_tokyo, event_pacific)
    print(result)