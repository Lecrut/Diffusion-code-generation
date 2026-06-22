import datetime

def days_remaining_in_month(year, month):
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if year < 1:
        raise ValueError("Year must be positive")
    
    if month == 12:
        next_month_start = datetime.date(year + 1, 1, 1)
    else:
        next_month_start = datetime.date(year, month + 1, 1)
    
    first_day_of_month = datetime.date(year, month, 1)
    last_day_of_month = next_month_start - datetime.timedelta(days=1)
    
    days_in_month = last_day_of_month.day
    
    today = datetime.date.today()
    
    if today.month != month or today.year != year:
        return days_in_month
    
    days_passed = today.day
    remaining = days_in_month - days_passed
    
    if remaining < 0:
        return 0
    
    return remaining

if __name__ == '__main__':
    sample_dates = [
        (2023, 2),
        (2024, 2),
        (2023, 12),
        (2023, 1),
    ]
    
    for y, m in sample_dates:
        result = days_remaining_in_month(y, m)
        print(result)