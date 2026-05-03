from datetime import datetime
import pytz
def calculate_time_difference(tz_str1, tz_str2):
    tz1 = pytz.timezone(tz_str1)
    tz2 = pytz.timezone(tz_str2)
    reference_date = datetime(2023, 1, 1)
    dt1 = reference_date.replace(tzinfo=tz1)
    dt2 = reference_date.replace(tzinfo=tz2)
    utc1 = dt1.astimezone(pytz.utc)
    utc2 = dt2.astimezone(pytz.utc)
    diff_seconds = abs(utc1.timestamp() - utc2.timestamp())
    diff_hours = diff_seconds / 3600.0
    return diff_hours
if __name__ == '__main__':
    tz1_config = "America/New_York"
    tz2_config = "Europe/London"
    difference = calculate_time_difference(tz1_config, tz2_config)
    print(difference)