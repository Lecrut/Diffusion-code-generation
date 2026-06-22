import calendar
from datetime import datetime, timedelta

def calculate_days_remaining_in_month(target_year: int, target_month: int, current_day: int) -> int:
    if not isinstance(target_year, int) or not isinstance(target_month, int) or not isinstance(current_day, int):
        raise TypeError("Arguments must be integers")
    if not (1 <= target_month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= current_day <= 31):
        raise ValueError("Day must be between 1 and 31")
    
    last_day_of_month = calendar.monthrange(target_year, target_month)[1]
    if current_day > last_day_of_month:
        raise ValueError(f"Day {current_day} is invalid for month {target_month} of year {target_year}")
    
    current_date = datetime(target_year, target_month, current_day)
    next_month_first = (current_date.replace(day=1) + timedelta(days=32)).replace(day=1)
    days_remaining = (next_month_first - current_date).days
    return days_remaining

if __name__ == '__main__':
    sample_year = 2024
    sample_month = 2
    sample_day = 29
    result = calculate_days_remaining_in_month(sample_year, sample_month, sample_day)
    print(result)