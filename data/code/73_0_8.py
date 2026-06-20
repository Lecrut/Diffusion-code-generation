from datetime import datetime
import pytz

def calculate_time_difference(dt1, dt2, tz1, tz2):
    timezone1 = pytz.timezone(tz1)
    timezone2 = pytz.timezone(tz2)
    
    dt1 = timezone1.localize(dt1)
    dt2 = timezone2.localize(dt2)
    
    dt1_utc = dt1.astimezone(pytz.utc)
    dt2_utc = dt2.astimezone(pytz.utc)
    
    return abs((dt1_utc - dt2_utc).total_seconds())

if __name__ == '__main__':
    sample_dt1 = datetime(2023, 4, 1, 12, 0, 0)
    sample_dt2 = datetime(2023, 4, 1, 15, 0, 0)
    sample_tz1 = 'America/New_York'
    sample_tz2 = 'Asia/Tokyo'
    
    print(calculate_time_difference(sample_dt1, sample_dt2, sample_tz1, sample_tz2))