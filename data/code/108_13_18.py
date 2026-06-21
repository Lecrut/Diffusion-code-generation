from datetime import date
import calendar

def validate_date(year: int, month: int, day: int) -> None:
    if not isinstance(year, int) or isinstance(year, bool):
        raise ValueError("Year must be an integer")
    if not isinstance(month, int) or isinstance(month, bool):
        raise ValueError("Month must be an integer")
    if not isinstance(day, int) or isinstance(day, bool):
        raise ValueError("Day must be an integer")
    if not (1 <= month <= 12):
        raise ValueError("Month out of range")
    if not (1 <= day <= 31):
        raise ValueError("Day out of range")
    days_in_month = calendar.monthrange(year, month)[1]
    if day > days_in_month:
        raise ValueError("Day out of range for given month and year")

def get_day_of_month(year: int, month: int, day: int) -> int:
    validate_date(year, month, day)
    return date(year, month, day).day

if __name__ == '__main__':
    result = get_day_of_month(2024, 10, 10)
    print(result)