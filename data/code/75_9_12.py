from datetime import datetime

def date_difference_days(date1: datetime, date2: datetime) -> int:
    if date1 > date2:
        raise ValueError("date1 must be before date2")
    delta = date2 - date1
    return delta.days

if __name__ == '__main__':
    sample_date1 = datetime(2023, 10, 26)
    sample_date2 = datetime(2024, 11, 26)
    print(date_difference_days(sample_date1, sample_date2))