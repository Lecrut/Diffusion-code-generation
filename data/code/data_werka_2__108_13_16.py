from datetime import date

def get_numeric_day(year: int, month: int, day: int) -> int:
    if not (1 <= month <= 12):
        raise ValueError(f"Invalid month: {month}")
    if not (1 <= day <= 31):
        raise ValueError(f"Invalid day: {day}")
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise TypeError("Arguments must be integers")
    try:
        target = date(year, month, day)
    except ValueError as exc:
        raise ValueError(f"Cannot construct date: {exc}")
    return target.day

if __name__ == '__main__':
    year_val = 2024
    month_val = 10
    day_val = 10
    result = get_numeric_day(year_val, month_val, day_val)
    print(result)