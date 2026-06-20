from datetime import datetime

def compare_datetimes(dt1: datetime, dt2: datetime) -> bool:
    return dt1 == dt2

if __name__ == '__main__':
    sample_dt1 = datetime(2023, 10, 5, 14, 30, 0)
    sample_dt2 = datetime(2023, 10, 5, 14, 30, 0)
    result = compare_datetimes(sample_dt1, sample_dt2)
    print(result)