import calendar
from datetime import datetime

def is_weekday(dt: datetime) -> bool:
    return dt.weekday() < 5
if __name__ == '__main__':
    sample_dt1 = datetime(2023, 10, 10)
    sample_dt2 = datetime(2023, 10, 11)
    print(is_weekday(sample_dt1))
    print(is_weekday(sample_dt2))