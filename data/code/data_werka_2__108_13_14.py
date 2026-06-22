from datetime import date
import calendar

def _validate_date_components(year: int, month: int, day: int) -> None:
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise TypeError("Year, month, and day must be integers")
    if not (1 <= month <= 12):
        raise ValueError(f"Invalid month: {month}")
    if not (1 <= day <= 31):
        raise ValueError(f"Invalid day: {day}")
    max_days = calendar.monthrange(year, month)[1]
    if day > max_days:
        raise ValueError(f"Invalid day {day} for month {month} in year {year}")

def get_day_of_month(year: int, month: int, day: int) -> int:
    _validate_date_components(year, month, day)
    return date(year, month, day).day

if __name__ == '__main__':
    target_year = 2024
    target_month = 10
    target_day = 10
    result = get_day_of_month(target_year, target_month, target_day)
    print(result)