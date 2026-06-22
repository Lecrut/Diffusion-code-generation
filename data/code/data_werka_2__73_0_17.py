import pytz
from datetime import datetime

def calculate_time_difference(dt1_str, dt1_tz_name, dt2_str, dt2_tz_name):
    tz1 = pytz.timezone(dt1_tz_name)
    tz2 = pytz.timezone(dt2_tz_name)
    
    dt1 = tz1.localize(datetime.strptime(dt1_str, "%Y-%m-%d %H:%M:%S"))
    dt2 = tz2.localize(datetime.strptime(dt2_str, "%Y-%m-%d %H:%M:%S"))
    
    dt1_utc = dt1.astimezone(pytz.utc)
    dt2_utc = dt2.astimezone(pytz.utc)
    
    delta = dt2_utc - dt1_utc
    return delta

if __name__ == '__main__':
    result = calculate_time_difference("2023-10-01 12:00:00", "US/Eastern", "2023-10-01 12:00:00", "Europe/London")
    print(result)