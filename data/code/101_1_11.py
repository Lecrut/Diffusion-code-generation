import calendar
from datetime import date

def get_weekday_name(year, month, day):
    if not (1 <= month <= 12):
        raise ValueError(f"Invalid month: {month}")
    if day < 1:
        raise ValueError(f"Invalid day: {day}")
    
    try:
        d = date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date: {year}-{month}-{day}") from e
    
    return calendar.day_name[d.weekday()]

if __name__ == '__main__':
    result = get_weekday_name(2023, 10, 5)
    print(result)