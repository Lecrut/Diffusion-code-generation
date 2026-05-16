import datetime
import pytz
def calculate_time_difference(dt1, dt2):
    if dt1.tzinfo is None or dt2.tzinfo is None:
        raise ValueError("One or both datetime objects are naive (no timezone information).")
    if dt1.tzinfo != dt2.tzinfo:
        raise ValueError("Timezones of the two datetime objects are different.")
    dt1_utc = dt1.astimezone(pytz.utc)
    dt2_utc = dt2.astimezone(pytz.utc)
    difference = dt2_utc - dt1_utc
    return difference
if __name__ == '__main__':
    tz_london = pytz.timezone('Europe/London')
    tz_new_york = pytz.timezone('America/New_York')
    dt_london_time = datetime.datetime(2023, 10, 26, 10, 0, 0, tzinfo=tz_london)
    dt_new_york_time = datetime.datetime(2023, 10, 26, 5, 0, 0, tzinfo=tz_new_york)
    try:
        time_diff = calculate_time_difference(dt_london_time, dt_new_york_time)
        print(f"Datetime 1 (London): {dt_london_time}")
        print(f"Datetime 2 (New York): {dt_new_york_time}")
        print(f"Time difference (Datetime 2 - Datetime 1): {time_diff}")
    except ValueError as e:
        print(f"Error: {e}")