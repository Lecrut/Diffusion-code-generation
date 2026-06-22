import calendar
import datetime

def get_day_of_week(year: int, month: int, day: int) -> str:
    if not 1 <= month <= 12:
        raise ValueError("Month out of range")
    if not 1 <= day <= 31:
        raise ValueError("Day out of range")
    try:
        date_obj = datetime.date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date: {e}")
    return calendar.day_name[date_obj.weekday()]

if __name__ == '__main__':
    result = get_day_of_week(2025, 3, 15)
    print(result)