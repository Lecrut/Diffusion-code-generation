import datetime
import pytz
def convert_timezone(dt_object, target_tz_str):
    if dt_object.tzinfo is None or dt_object.tzinfo.utcoffset(dt_object) is None:
        dt_object = pytz.timezone(dt_object.tzname).localize(dt_object)
    target_tz = pytz.timezone(target_tz_str)
    if dt_object.tzinfo != target_tz:
        converted_dt = dt_object.astimezone(target_tz)
        return converted_dt
    else:
        return dt_object
if __name__ == '__main__':
    sample_datetime_naive = datetime.datetime(2023, 10, 27, 10, 30, 0)
    sample_tz_name = "America/New_York"
    target_tz_name = "Europe/London"
    try:
        sample_datetime_aware = pytz.timezone(sample_tz_name).localize(sample_datetime_naive)
        converted_time = convert_timezone(sample_datetime_aware, target_tz_name)
        print(f"Original Time (in {sample_tz_name}): {sample_datetime_aware}")
        print(f"Converted Time (in {target_tz_name}): {converted_time}")
    except Exception as e:
        print(f"An error occurred: {e}")