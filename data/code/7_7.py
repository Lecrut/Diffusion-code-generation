import datetime
import pytz

def convert_timezone(dt_obj, target_zone_name):
    if dt_obj.tzinfo is None:
        dt_obj = pytz.utc.localize(dt_obj)
    target_tz = pytz.timezone(target_zone_name)
    converted_dt = dt_obj.astimezone(target_tz)
    return converted_dt

if __name__ == '__main__':
    now_utc = datetime.datetime.now(pytz.utc)
    result = convert_timezone(now_utc, 'America/New_York')
    print(result.strftime('%Y-%m-%d %H:%M:%S %Z'))