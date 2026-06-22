import datetime

def days_remaining_in_month(year: int, month: int) -> int:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if year < 1:
        raise ValueError("Year must be positive")
    
    if month == 12:
        next_month = datetime.date(year + 1, 1, 1)
    else:
        next_month = datetime.date(year, month + 1, 1)
    
    first_day_of_next_month = next_month
    first_day_of_current_month = datetime.date(year, month, 1)
    
    days_in_month = (first_day_of_next_month - first_day_of_current_month).days
    
    today = datetime.date.today()
    if today.month == month and today.year == year:
        days_passed = (today - first_day_of_current_month).days
        return days_in_month - days_passed - 1
    elif today < first_day_of_current_month:
        return days_in_month
    else:
        return 0

if __name__ == '__main__':
    sample_dates = [
        (2023, 2),
        (2024, 2),
        (2023, 12),
        (2023, 1),
    ]
    
    for y, m in sample_dates:
        result = days_remaining_in_month(y, m)
        print(f"Days remaining in {y}-{m:02d}: {result}")
    
    current_year = datetime.date.today().year
    current_month = datetime.date.today().month
    current_result = days_remaining_in_month(current_year, current_month)
    print(f"Days remaining in current month {current_year}-{current_month:02d}: {current_result}")