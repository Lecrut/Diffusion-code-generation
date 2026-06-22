from datetime import date
import calendar

def get_day_of_month(year: int, month: int, day: int) -> int:
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise TypeError("Year, month, and day must be integers")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= day <= 31):
        raise ValueError("Day must be between 1 and 31")
    max_days = calendar.monthrange(year, month)[1]
    if day > max_days:
        raise ValueError(f"Day {day} is invalid for month {month} in year {year}")
    return date(year, month, day).day

if __name__ == '__main__':
    result = get_day_of_month(2024, 10, 10)
    print(result)