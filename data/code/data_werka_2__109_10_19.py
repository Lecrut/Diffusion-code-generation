import datetime

DAYS_IN_WEEK = 7
MIN_MONTH = 1
MAX_MONTH = 12
MIN_YEAR = 1
TIMedelta_DAYS = 1

def get_days_remaining_in_month(year, month):
    if not (MIN_MONTH <= month <= MAX_MONTH):
        raise ValueError("Month must be between 1 and 12")
    if year < MIN_YEAR:
        raise ValueError("Year must be positive")
    
    if month == MAX_MONTH:
        next_month_start = datetime.date(year + 1, MIN_MONTH, MIN_MONTH)
    else:
        next_month_start = datetime.date(year, month + MIN_MONTH, MIN_MONTH)
    
    last_day_current = next_month_start - datetime.timedelta(days=TIMedelta_DAYS)
    today = datetime.date.today()
    
    if today > last_day_current:
        return 0
    
    return (last_day_current - today).days

if __name__ == '__main__':
    test_cases = [
        (2023, 10),
        (2024, 2),
        (2023, 12),
        (2025, 1)
    ]
    for y, m in test_cases:
        result = get_days_remaining_in_month(y, m)
        print(f"Year: {y}, Month: {m}, Days Remaining: {result}")