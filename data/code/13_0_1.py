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
    tz_london = pytz.timezone('Europe/London')
    tz_tokyo = pytz.timezone('Asia/Tokyo')
    dt_london = datetime.datetime(2023, 10, 26, 10, 0, 0, tzinfo=tz_london)
    dt_tokyo = datetime.datetime(2023, 10, 26, 20, 0, 0, tzinfo=tz_tokyo)
    try:
        time_diff = calculate_time_difference(dt_london, dt_tokyo)
        print(f"Datetime 1 (London): {dt_london}")
        print(f"Datetime 2 (Tokyo): {dt_tokyo}")
        print(f"Time difference (Tokyo - London): {time_diff}")
    except ValueError as e:
        print(f"Error: {e}")