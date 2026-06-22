import pytz
from datetime import datetime

def calculate_time_difference(timezone1, timezone2):
    tz1 = pytz.timezone(timezone1)
    tz2 = pytz.timezone(timezone2)
    now_tz1 = datetime.now(tz1)
    now_tz2 = datetime.now(tz2)
    difference = (now_tz1.utcoffset() - now_tz2.utcoffset()).total_seconds() / 3600
    return abs(difference)
if __name__ == '__main__':
    timezone1 = 'America/New_York'
    timezone2 = 'Europe/London'
    difference_in_hours = calculate_time_difference(timezone1, timezone2)
    print(difference_in_hours)