import datetime
import pytz
def calculate_duration_minutes(date_str1, time_str1, date_str2, time_str2):
    tz = pytz.utc
    format_str = "%Y-%m-%d %H:%M:%S"
    try:
        dt1 = datetime.datetime.strptime(f"{date_str1} {time_str1}", format_str)
        dt2 = datetime.datetime.strptime(f"{date_str2} {time_str2}", format_str)
    except ValueError as e:
        raise ValueError(f"Date/Time format error: {e}")
    dt1_aware = tz.localize(dt1)
    dt2_aware = tz.localize(dt2)
    duration = dt2_aware - dt1_aware
    duration_minutes = duration.total_seconds() / 60
    return duration_minutes
if __name__ == '__main__':
    date1 = "2023-01-01"
    time1 = "10:00:00"
    date2 = "2023-01-01"
    time2 = "12:30:00"
    try:
        result = calculate_duration_minutes(date1, time1, date2, time2)
        print(result)
    except ValueError as e:
        print(e)