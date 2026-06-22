import calendar
from datetime import datetime, date

def calculate_days_remaining(year: int, month: int, day: int) -> int:
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise TypeError("Year, month, and day must be integers")
    if not (1 <= month <= 12):
        raise ValueError(f"Invalid month: {month}")
    try:
        date(year, month, day)
    except ValueError:
        raise ValueError(f"Invalid date: {year}-{month}-{day}")
    
    last_day = calendar.monthrange(year, month)[1]
    return last_day - day

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 15
    remaining = calculate_days_remaining(sample_year, sample_month, sample_day)
    print(remaining)