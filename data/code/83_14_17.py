from datetime import datetime

def validate_datetime(dt):
    if not isinstance(dt, datetime):
        raise ValueError("Both arguments must be instances of datetime")

def compare_datetimes(dt1, dt2):
    validate_datetime(dt1)
    validate_datetime(dt2)
    return dt1 == dt2

if __name__ == '__main__':
    sample_dt1 = datetime(2023, 10, 5, 14, 30)
    sample_dt2 = datetime(2023, 10, 5, 14, 30)
    print(compare_datetimes(sample_dt1, sample_dt2))