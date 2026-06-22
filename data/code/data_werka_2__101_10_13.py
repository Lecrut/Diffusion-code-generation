import calendar
from datetime import date

def determine_weekday(year: int, month: int, day: int) -> str:
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("Arguments must be integers")
    try:
        target_date = date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date: {year}-{month}-{day}") from e
    return target_date.strftime("%A")

if __name__ == '__main__':
    year = 2023
    month = 12
    day = 25
    weekday_name = determine_weekday(year, month, day)
    print(weekday_name)