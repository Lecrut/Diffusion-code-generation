from datetime import date
from calendar import isleap

FULL_YEAR_DAYS_COMMON = 365
FULL_YEAR_DAYS_LEAP = 366
MINUS_ONE = -1

def calculate_full_years(start_date: date, end_date: date) -> int:
    if start_date > end_date:
        raise ValueError("start_date must be before or equal to end_date")
    if start_date == end_date:
        return 0
    years_count = 0
    current_date = start_date
    while current_date <= end_date:
        next_year = current_date.year + 1
        try:
            next_anniversary = date(next_year, current_date.month, current_date.day)
        except ValueError:
            next_anniversary = date(next_year, current_date.month, 28)
        if next_anniversary > end_date:
            break
        years_count += 1
        current_date = next_anniversary
    return years_count

if __name__ == '__main__':
    start = date(1990, 5, 15)
    end = date(2023, 5, 14)
    result = calculate_full_years(start, end)
    print(result)