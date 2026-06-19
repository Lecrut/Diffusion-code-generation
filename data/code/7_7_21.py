import pytz
from datetime import datetime

def convert_timezone(dt, target_tz):
    source_tz = dt.tzinfo
    if not source_tz:
        raise ValueError('Input datetime must have timezone information.')
    target_timezone = pytz.timezone(target_tz)
    localized_dt = source_tz.localize(dt) if isinstance(source_tz, str) else dt.astimezone(pytz.utc).astimezone(target_timezone)
    return localized_dt
if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, tzinfo=pytz.timezone('UTC'))
    target_timezone = 'America/New_York'
    converted_time = convert_timezone(sample_dt, target_timezone)
    print(converted_time)