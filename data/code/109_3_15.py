import calendar
from datetime import datetime

def get_days_remaining_in_month(year: int, month: int, day: int) -> int:
    last_day_of_month = calendar.monthrange(year, month)[1]
    days_remaining = last_day_of_month - day
    return days_remaining

if __name__ == '__main__':
    sample_year = 2024
    sample_month = 2
    sample_day = 10
    remaining = get_days_remaining_in_month(sample_year, sample_month, sample_day)
    print(remaining)