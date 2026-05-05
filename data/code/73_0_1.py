import datetime
import pytz
def calculate_time_difference(dt1, dt2):
    if dt1.tzinfo is None or dt2.tzinfo is None:
        raise ValueError("Both datetime objects must be timezone-aware.")
    dt1_utc = dt1.astimezone(pytz.utc)
    dt2_utc = dt2.astimezone(pytz.utc)
    difference = dt2_utc - dt1_utc
    return difference
if __name__ == '__main__':
    tz_ny = pytz.timezone('America/New_York')
    tz_london = pytz.timezone('Europe/London')
    dt_ny = datetime.datetime(2023, 10, 26, 10, 0, 0, tzinfo=tz_ny)
    dt_london = datetime.datetime(2023, 10, 26, 15, 0, 0, tzinfo=tz_london)
    try:
        time_diff = calculate_time_difference(dt_ny, dt_london)
        print(f"Datetime 1 (NY): {dt_ny}")
        print(f"Datetime 2 (London): {dt_london}")
        print(f"Time difference (London - NY): {time_diff}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")