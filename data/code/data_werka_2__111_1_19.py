from datetime import date, timedelta
from calendar import monthrange

DATE_FORMAT = "%Y-%m-%d"
JULY = 7
FOURTH = 4
YEAR = 2024
DAYS_INCREMENT = 30

def validate_date(year: int, month: int, day: int) -> date:
    if month < 1 or month > 12:
        raise ValueError("Invalid month")
    max_day = monthrange(year, month)[1]
    if day < 1 or day > max_day:
        raise ValueError("Invalid day")
    return date(year, month, day)

def add_days_to_date(start_date: date, days: int) -> str:
    result = start_date + timedelta(days=days)
    return result.strftime(DATE_FORMAT)

def compute_future_date(year: int, month: int, day: int, days_to_add: int) -> str:
    initial = validate_date(year, month, day)
    return add_days_to_date(initial, days_to_add)

if __name__ == '__main__':
    result = compute_future_date(YEAR, JULY, FOURTH, DAYS_INCREMENT)
    print(result)