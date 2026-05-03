import datetime
import pytz
def calculate_time_difference(dt1_str, tz1_str, dt2_str, tz2_str):
    tz1 = pytz.timezone(tz1_str)
    tz2 = pytz.timezone(tz2_str)
    dt1 = pytz.datetime.datetime.fromisoformat(dt1_str)
    dt2 = pytz.datetime.datetime.fromisoformat(dt2_str)
    dt1_aware = dt1.astimezone(tz1)
    dt2_aware = dt2.astimezone(tz2)
    dt1_utc = dt1_aware.astimezone(pytz.utc)
    dt2_utc = dt2_aware.astimezone(pytz.utc)
    time_difference = dt2_utc - dt1_utc
    return time_difference
if __name__ == '__main__':
    datetime1_str = "2023-10-27T10:00:00"
    timezone1_str = "America/New_York"
    datetime2_str = "2023-10-27T14:30:00"
    timezone2_str = "Europe/London"
    difference = calculate_time_difference(datetime1_str, timezone1_str, datetime2_str, timezone2_str)
    print(f"Datetime 1: {datetime1_str} in {timezone1_str}")
    print(f"Datetime 2: {datetime2_str} in {timezone2_str}")
    print(f"Time Difference (Datetime 2 - Datetime 1): {difference}")
    print(f"Time Difference in hours: {difference.total_seconds() / 3600}")
    print(f"Time Difference in days: {difference.total_seconds() / 86400}")