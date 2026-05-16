from datetime import datetime
import pytz
def calculate_time_difference(tz_str1, tz_str2):
    tz1 = pytz.timezone(tz_str1)
    tz2 = pytz.timezone(tz_str2)
    reference_time_utc = datetime(2023, 1, 1, 12, 0, 0, tzinfo=pytz.utc)
    time1 = reference_time_utc.astimezone(tz1)
    time2 = reference_time_utc.astimezone(tz2)
    diff_seconds = (time1 - time2).total_seconds()
    diff_hours = diff_seconds / 3600
    return diff_hours
if __name__ == '__main__':
    tz1_config = "America/Los_Angeles"
    tz2_config = "Europe/London"
    difference = calculate_time_difference(tz1_config, tz2_config)
    print(difference)