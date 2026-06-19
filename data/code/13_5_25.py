import pytz
from datetime import datetime

def get_timezone_difference(config_data):
    timezone1, timezone2 = config_data.split(',')
    tz1 = pytz.timezone(timezone1.strip())
    tz2 = pytz.timezone(timezone2.strip())
    utc_now = datetime.now(pytz.utc)
    local_time1 = utc_now.astimezone(tz1)
    local_time2 = utc_now.astimezone(tz2)
    difference = (local_time2 - local_time1).total_seconds() / 3600
    return abs(difference)
if __name__ == '__main__':
    config_data = 'America/New_York, Europe/London'
    difference_hours = get_timezone_difference(config_data)
    print(difference_hours)