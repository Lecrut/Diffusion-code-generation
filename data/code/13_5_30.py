import pytz
from datetime import datetime

def calculate_timezone_difference(config):
    timezone1 = config.get('timezone1', 'UTC')
    timezone2 = config.get('timezone2', 'UTC')
    
    tz1 = pytz.timezone(timezone1)
    tz2 = pytz.timezone(timezone2)
    
    now = datetime.now()
    time1 = tz1.localize(now).astimezone(pytz.utc)
    time2 = tz2.localize(now).astimezone(pytz.utc)
    
    difference_hours = (time2 - time1).total_seconds() / 3600
    return abs(difference_hours)

if __name__ == '__main__':
    config = {
        'timezone1': 'America/New_York',
        'timezone2': 'Europe/London'
    }
    print(calculate_timezone_difference(config))