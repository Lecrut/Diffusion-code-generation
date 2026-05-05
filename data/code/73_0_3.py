import datetime
import pytz
def calculate_time_difference(dt1, dt2):
    if dt1.tzinfo is None or dt2.tzinfo is None:
        raise ValueError("Both datetime objects must be timezone-aware.")
    dt1_utc = dt1.astimezone(pytz.utc)
    dt2_utc = dt2.astimezone(pytz.utc)
    time_difference = dt2_utc - dt1_utc
    return time_difference
if __name__ == '__main__':
    tz_london = pytz.timezone('Europe/London')
    tz_new_york = pytz.timezone('America/New_York')
    dt_london = datetime.datetime(2023, 10, 26, 10, 0, 0, tzinfo=tz_london)
    dt_new_york = datetime.datetime(2023, 10, 26, 5, 0, 0, tzinfo=tz_new_york)
    try:
        diff = calculate_time_difference(dt_london, dt_new_york)
        print(f"Datetime 1 (London): {dt_london}")
        print(f"Datetime 2 (New York): {dt_new_york}")
        print(f"Time difference (Datetime 2 - Datetime 1): {diff}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")