from datetime import date, timedelta
import calendar

def add_days_to_date(target_date: date, days_to_add: int) -> str:
    if target_date is None:
        raise ValueError("Date cannot be None")
    if not isinstance(days_to_add, int):
        raise ValueError("Days must be an integer")
    end_date = target_date + timedelta(days=days_to_add)
    return end_date.strftime("%Y-%m-%d")

def create_date(year: int, month: int, day: int) -> date:
    if year < 1 or year > 9999:
        raise ValueError("Year out of range")
    if month < 1 or month > 12:
        raise ValueError("Month out of range")
    max_day = calendar.monthrange(year, month)[1]
    if day < 1 or day > max_day:
        raise ValueError("Day out of range")
    return date(year, month, day)

if __name__ == '__main__':
    base = create_date(2024, 7, 4)
    result = add_days_to_date(base, 30)
    print(result)