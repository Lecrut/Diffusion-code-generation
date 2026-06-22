import datetime

MIN_YEAR = 1
MAX_MONTH = 12
MIN_MONTH = 1
DAYS_IN_WEEK = 7
DEFAULT_DAY_OFFSET = 10

def calculate_remaining_days(year, month, day=None):
    if year < MIN_YEAR:
        raise ValueError("Year must be positive")
    if month < MIN_MONTH or month > MAX_MONTH:
        raise ValueError("Month must be between 1 and 12")
    
    if day is None:
        day = DEFAULT_DAY_OFFSET
        
    if day < 1:
        raise ValueError("Day must be positive")
        
    try:
        current_date = datetime.date(year, month, day)
    except ValueError:
        raise ValueError("Invalid date combination")
        
    if current_date.month != month:
        adjusted_day = current_date.day - (current_date.month - month) * 31
        current_date = datetime.date(year, month, adjusted_day)
        
    if current_date.day > 28:
        try:
            next_month_date = datetime.date(year, month + 1, 1)
        except ValueError:
            next_month_date = datetime.date(year + 1, 1, 1)
    else:
        next_month_date = datetime.date(year, month + 1, 1)
        
    last_day = next_month_date - datetime.timedelta(days=1)
    
    if current_date > last_day:
        return 0
        
    remaining = (last_day - current_date).days
    return remaining

if __name__ == '__main__':
    results = []
    test_cases = [
        (2023, 2, 10),
        (2024, 2, 29),
        (2023, 12, 31),
        (2023, 1, 1),
        (2000, 2, 15)
    ]
    
    for y, m, d in test_cases:
        val = calculate_remaining_days(y, m, d)
        results.append(val)
        
    print(results)