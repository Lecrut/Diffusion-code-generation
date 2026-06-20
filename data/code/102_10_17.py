import datetime

def is_weekday(dt):
    if not isinstance(dt, datetime.datetime):
        raise ValueError("Input must be an instance of datetime.datetime")
    return dt.weekday() < 5

if __name__ == '__main__':
    sample_dt = datetime.datetime(2023, 10, 10)
    print(is_weekday(sample_dt))