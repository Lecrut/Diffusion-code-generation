from datetime import datetime

def date_difference_days(date1: datetime, date2: datetime) -> int:
    delta = abs(date2 - date1)
    return delta.days
if __name__ == '__main__':
    sample_date1 = datetime(2023, 10, 26, 14, 30)
    sample_date2 = datetime(2023, 11, 26, 9, 45)
    result = date_difference_days(sample_date1, sample_date2)
    print(result)