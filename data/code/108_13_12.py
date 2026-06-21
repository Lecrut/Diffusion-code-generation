from datetime import date

def get_numeric_day(year: int, month: int, day: int) -> int:
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise TypeError("Year, month, and day must be integers")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= day <= 31):
        raise ValueError("Day must be between 1 and 31")
    try:
        d = date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date: {e}")
    return d.day

if __name__ == '__main__':
    target_year = 2024
    target_month = 10
    target_day = 10
    day_value = get_numeric_day(target_year, target_month, target_day)
    print(day_value)