from datetime import datetime

def is_same_day(date1: datetime, date2: datetime) -> bool:
    return date1.date() == date2.date()
if __name__ == '__main__':
    sample_date1 = datetime(2023, 4, 15, 12, 30)
    sample_date2 = datetime(2023, 4, 15, 9, 45)
    print(is_same_day(sample_date1, sample_date2))