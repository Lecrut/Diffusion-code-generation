import datetime
import pytz
if __name__ == '__main__':
    start_time_str = "2023-01-01 10:00:00+00:00"
    end_time_str = "2023-01-03 14:30:00+00:00"
    start_time = datetime.datetime.fromisoformat(start_time_str)
    end_time = datetime.datetime.fromisoformat(end_time_str)
    if start_time.tzinfo is None or end_time.tzinfo is None:
        raise ValueError("Input datetime objects must be timezone aware.")
    if end_time < start_time:
        elapsed_time = (end_time - start_time).total_seconds() / 3600
    else:
        elapsed_time = (end_time - start_time).total_seconds() / 3600
    print(f"{elapsed_time}")