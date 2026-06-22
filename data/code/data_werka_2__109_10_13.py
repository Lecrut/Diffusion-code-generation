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
    last_day_of_current_month = first_day_of_next_month - datetime.timedelta(days=1)
    
    return last_day_of_current_month.day

if __name__ == '__main__':
    sample_dates = [
        (2023, 2),
        (2024, 2),
        (2023, 12),
        (2023, 1),
        (2020, 4)
    ]
    
    for year, month in sample_dates:
        remaining_days = days_remaining_in_month(year, month)
        print(f"Year: {year}, Month: {month}, Days Remaining: {remaining_days}")