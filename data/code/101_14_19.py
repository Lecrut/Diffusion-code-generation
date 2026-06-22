import calendar
import datetime

def get_weekday_for_date(year: int, month: int, day: int) -> str:
    if not 1 <= month <= 12:
        raise ValueError("Invalid month")
    if not 1 <= day <= 31:
        raise ValueError("Invalid day")
    date_obj = datetime.date(year, month, day)
    return calendar.day_name[date_obj.weekday()]

if __name__ == '__main__':
    year_val = 2025
    month_val = 3
    day_val = 15
    day_name = get_weekday_for_date(year_val, month_val, day_val)
    print(day_name)