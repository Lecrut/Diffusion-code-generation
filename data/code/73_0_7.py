import pytz
from datetime import datetime, timedelta

def calculate_time_difference(start_dt, end_dt):
    if start_dt.tzinfo is None:
        start_dt = pytz.utc.localize(start_dt)
    if end_dt.tzinfo is None:
        end_dt = pytz.utc.localize(end_dt)
    
    start_utc = start_dt.astimezone(pytz.utc)
    end_utc = end_dt.astimezone(pytz.utc)
    
    delta = end_utc - start_utc
    total_seconds = int(delta.total_seconds())
    
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds = remaining_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    return {
        'total_seconds': total_seconds,
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
        'timedelta': delta
    }

if __name__ == '__main__':
    tz_ny = pytz.timezone('America/New_York')
    tz_london = pytz.timezone('Europe/London')
    
    start_dt = datetime(2023, 10, 1, 12, 0, 0)
    end_dt = datetime(2023, 10, 1, 12, 0, 0)
    
    start_dt = tz_ny.localize(start_dt)
    end_dt = tz_london.localize(end_dt)
    
    result = calculate_time_difference(start_dt, end_dt)
    
    print(result['total_seconds'])
    print(result['days'])
    print(result['hours'])
    print(result['minutes'])
    print(result['seconds'])
    print(result['timedelta'])