import calendar
import datetime

def get_weekday_name(year: int, month: int, day: int) -> str:
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("Inputs must be integers")
    if month < 1 or month > 12:
        raise ValueError("Month out of range")
    if day < 1 or day > 31:
        raise ValueError("Day out of range")
    date_instance = datetime.date(year, month, day)
    weekday_index = date_instance.weekday()
    return calendar.day_name[weekday_index]

if __name__ == '__main__':
    computed_day = get_weekday_name(2025, 3, 15)
    print(computed_day)