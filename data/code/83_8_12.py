from datetime import datetime

def same_calendar_day(date1: datetime, date2: datetime) -> bool:
    return date1.date() == date2.date()
if __name__ == '__main__':
    date1 = datetime(2023, 4, 15, 12, 30)
    date2 = datetime(2023, 4, 15, 20, 45)
    date3 = datetime(2023, 4, 16, 9, 0)
    print(same_calendar_day(date1, date2))
    print(same_calendar_day(date1, date3))