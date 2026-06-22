import datetime

def days_remaining(year, month):
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    
    last_day_of_current_month = datetime.date(year, month, 1) - datetime.timedelta(days=1)
    first_day_of_next_month = datetime.date(next_year, next_month, 1)
    
    return (first_day_of_next_month - last_day_of_current_month).days

if __name__ == '__main__':
    test_cases = [
        (2023, 1),
        (2024, 2),
        (2024, 12),
        (2023, 12),
        (2024, 1),
    ]
    for year, month in test_cases:
        result = days_remaining(year, month)
        print(f"Days remaining in {year}-{month}: {result}")