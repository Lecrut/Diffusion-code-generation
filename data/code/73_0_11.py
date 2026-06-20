from datetime import datetime
import pytz

def calculate_time_difference(dt1, dt2):
    tz1 = pytz.timezone('America/New_York')
    tz2 = pytz.timezone('Asia/Shanghai')

    dt1 = dt1.replace(tzinfo=tz1)
    dt2 = dt2.replace(tzinfo=tz2)

    local_dt1 = dt1.astimezone(tz2)
    time_difference = local_dt1 - dt2

    return time_difference

if __name__ == '__main__':
    dt1 = datetime(2023, 4, 1, 12, 0, 0)
    dt2 = datetime(2023, 4, 1, 18, 0, 0)

    result = calculate_time_difference(dt1, dt2)
    print(result.total_seconds())