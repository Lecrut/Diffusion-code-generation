from datetime import datetime
import pytz

def calculate_time_difference(dt1, dt2, tz1='UTC', tz2='UTC'):
    tz1 = pytz.timezone(tz1)
    tz2 = pytz.timezone(tz2)
    
    dt1 = dt1.replace(tzinfo=pytz.utc).astimezone(tz1)
    dt2 = dt2.replace(tzinfo=pytz.utc).astimezone(tz2)
    
    return abs(dt1 - dt2)

if __name__ == '__main__':
    dt1 = datetime(2023, 10, 1, 12, 0, 0, tzinfo=pytz.timezone('America/New_York'))
    dt2 = datetime(2023, 10, 1, 18, 0, 0, tzinfo=pytz.timezone('Asia/Tokyo'))
    
    print(calculate_time_difference(dt1, dt2))