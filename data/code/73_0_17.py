from datetime import datetime
import pytz

def calculate_time_difference(dt1_str, dt2_str, tz1, tz2):
    tz1 = pytz.timezone(tz1)
    tz2 = pytz.timezone(tz2)

    dt1 = datetime.strptime(dt1_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=pytz.utc).astimezone(tz1)
    dt2 = datetime.strptime(dt2_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=pytz.utc).astimezone(tz2)

    return abs((dt2 - dt1).total_seconds())

if __name__ == '__main__':
    sample_dt1 = '2023-04-01 12:00:00'
    sample_dt2 = '2023-04-01 15:30:00'
    sample_tz1 = 'America/New_York'
    sample_tz2 = 'Asia/Shanghai'

    print(calculate_time_difference(sample_dt1, sample_dt2, sample_tz1, sample_tz2))