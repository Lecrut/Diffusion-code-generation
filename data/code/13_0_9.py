import datetime
import pytz
def calculate_time_difference(dt1_str, tz1_str, dt2_str, tz2_str):
    tz1 = pytz.timezone(tz1_str)
    tz2 = pytz.timezone(tz2_str)
    dt1 = pytz.datetime.datetime.fromisoformat(dt1_str)
    dt2 = pytz.datetime.datetime.fromisoformat(dt2_str)
    dt1_aware = dt1.astimezone(tz1)
    dt2_aware = dt2.astimezone(tz2)
    diff = dt2_aware - dt1_aware
    return diff
if __name__ == '__main__':
    datetime1_str = "2023-10-27T10:00:00"
    tz1_str = "America/New_York"
    datetime2_str = "2023-10-27T14:30:00"
    tz2_str = "Europe/London"
    time_difference = calculate_time_difference(datetime1_str, tz1_str, datetime2_str, tz2_str)
    print(f"Datetime 1: {datetime1_str} in {tz1_str}")
    print(f"Datetime 2: {datetime2_str} in {tz2_str}")
    print(f"Time difference: {time_difference}")