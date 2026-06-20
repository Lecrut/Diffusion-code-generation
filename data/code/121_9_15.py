from datetime import datetime

def is_later_time(dt1, dt2):
    if not isinstance(dt1, datetime) or not isinstance(dt2, datetime):
        raise ValueError("Both inputs must be datetime objects.")
    return dt1 > dt2

if __name__ == '__main__':
    time1 = datetime(2023, 4, 15, 12, 0)
    time2 = datetime(2023, 4, 15, 12, 30)
    result = is_later_time(time2, time1)
    print(result)