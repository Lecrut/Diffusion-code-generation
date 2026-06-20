from datetime import datetime

def compare_datetimes_ignoring_time(dt1: datetime, dt2: datetime) -> bool:
    return dt1.date() == dt2.date()

if __name__ == '__main__':
    sample_dt1 = datetime(2023, 10, 27, 9, 15)
    sample_dt2 = datetime(2023, 10, 27, 14, 30)
    result = compare_datetimes_ignoring_time(sample_dt1, sample_dt2)
    print(result)