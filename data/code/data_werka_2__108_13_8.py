from datetime import date
import calendar

def get_day_of_month(year: int, month: int, day: int) -> int:
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise TypeError("Arguments must be integers")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    max_days = calendar.monthrange(year, month)[1]
    if not (1 <= day <= max_days):
        raise ValueError(f"Day must be between 1 and {max_days} for the given month and year")
    return date(year, month, day).day

if __name__ == '__main__':
    result = get_day_of_month(2024, 10, 10)
    print(result)