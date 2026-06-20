from datetime import datetime
import pytz

def calculate_time_difference(dt1, dt2):
    tz1 = pytz.timezone('America/New_York')
    tz2 = pytz.timezone('Asia/Shanghai')

    dt1 = tz1.localize(dt1)
    dt2 = tz2.localize(dt2)

    return abs((dt1 - dt2).total_seconds())

if __name__ == '__main__':
    sample_dt1 = datetime(2023, 4, 1, 12, 0, 0)
    sample_dt2 = datetime(2023, 4, 1, 18, 0, 0)

    print(calculate_time_difference(sample_dt1, sample_dt2))