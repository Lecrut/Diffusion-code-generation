from datetime import date
import calendar

def extract_day_numeric(year: int, month: int, day: int) -> int:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= day <= 31):
        raise ValueError("Day must be between 1 and 31")
    if not calendar.isleap(year) and month == 2 and day > 28:
        raise ValueError("Invalid day for February in a non-leap year")
    if month in (4, 6, 9, 11) and day > 30:
        raise ValueError("Invalid day for month with 30 days")
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise TypeError("Arguments must be integers")
    try:
        constructed = date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date: {e}")
    return constructed.day

if __name__ == '__main__':
    target_year = 2024
    target_month = 10
    target_day = 10
    computed_day = extract_day_numeric(target_year, target_month, target_day)
    print(computed_day)