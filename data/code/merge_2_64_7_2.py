import calendar
from datetime import date
def validate_date(year: int, month: int, day: int) -> bool:
    try:
        d = date(year, month, day)
        return True
    except ValueError:
        return False
def generate_month_string(year: int, month: int) -> str:
    if not validate_date(year, month, 1):
        raise ValueError(f"Invalid year or month for {year}/{month}")
    cal = calendar.Calendar()
    try:
        first_day = cal.monthdayscalendar(year, month)[0]
        return f"{first_day[0]:d} {cal.month_name(month)} {year}"
    except Exception as e:
        raise ValueError(f"Failed to generate date string for {year}/{month}: {e}")
if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    try:
        result = generate_month_string(sample_year, sample_month)
        print(result)
    except ValueError as ve:
        print(f"Validation Error: {ve}")