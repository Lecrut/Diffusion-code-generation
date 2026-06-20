from datetime import datetime

def is_same_day(date1: datetime, date2: datetime) -> bool:
    return date1.date() == date2.date()
if __name__ == '__main__':
    date1 = datetime(2023, 4, 15, 12, 30)
    date2 = datetime(2023, 4, 15, 18, 45)
    print(is_same_day(date1, date2))