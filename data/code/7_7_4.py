import datetime
import pytz
def convert_timezone(dt_object, target_tz_str):
    if dt_object.tzinfo is None or dt_object.tzinfo.utcoffset(dt_object) is None:
        dt_object = pytz.timezone(dt_object.tzname).localize(dt_object)
    target_tz = pytz.timezone(target_tz_str)
    converted_dt = dt_object.astimezone(target_tz)
    return converted_dt
if __name__ == '__main__':
    sample_datetime_str = "2023-10-27 10:00:00"
    sample_tz_str = "America/New_York"
    naive_dt = datetime.datetime.strptime(sample_datetime_str, "%Y-%m-%d %H:%M:%S")
    try:
        converted_time = convert_timezone(naive_dt, sample_tz_str)
        print(f"Original Datetime (Naive): {naive_dt}")
        print(f"Converted Datetime in {sample_tz_str}: {converted_time}")
    except Exception as e:
        print(f"An error occurred: {e}")