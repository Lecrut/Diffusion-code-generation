from datetime import datetime

def date_difference_days(date1: datetime, date2: datetime) -> int:
    return abs((date2 - date1).days)

if __name__ == '__main__':
    sample_date1 = datetime(2023, 1, 1)
    sample_date2 = datetime(2023, 1, 15)
    print(date_difference_days(sample_date1, sample_date2))