import datetime
import pytz
def calculate_time_difference(dt1_str, dt2_str, tz1_name, tz2_name):
    tz1 = pytz.timezone(tz1_name)
    tz2 = pytz.timezone(tz2_name)
    dt1 = pytz.timezone(tz1_name).localize(datetime.datetime.strptime(dt1_str, "%Y-%m-%d %H:%M:%S"))
    dt2 = pytz.timezone(tz2_name).localize(datetime.datetime.strptime(dt2_str, "%Y-%m-%d %H:%M:%S"))
    dt1_utc = dt1.astimezone(pytz.utc)
    dt2_utc = dt2.astimezone(pytz.utc)
    time_difference = dt2_utc - dt1_utc
    return time_difference
if __name__ == '__main__':
    time_string1 = "2023-10-27 10:00:00"
    time_string2 = "2023-10-27 14:30:00"
    timezone1 = "America/New_York"
    timezone2 = "Europe/London"
    difference = calculate_time_difference(time_string1, time_string2, timezone1, timezone2)
    print(f"Time 1: {time_string1} in {timezone1}")
    print(f"Time 2: {time_string2} in {timezone2}")
    print(f"Time difference (Time 2 - Time 1): {difference}")
    print(f"Time difference in total seconds: {difference.total_seconds()}")