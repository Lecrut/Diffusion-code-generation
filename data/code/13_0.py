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
    date1_str = "2023-10-26 10:00:00"
    date2_str = "2023-10-26 14:30:00"
    timezone1 = "America/New_York"
    timezone2 = "Europe/London"
    difference = calculate_time_difference(date1_str, date2_str, timezone1, timezone2)
    print(f"Date 1: {date1_str} in {timezone1}")
    print(f"Date 2: {date2_str} in {timezone2}")
    print(f"Time difference (Date 2 - Date 1): {difference}")