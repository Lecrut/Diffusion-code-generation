import datetime

def calculate_days_remaining_in_month(target_date):
    if target_date is None:
        raise ValueError("Target date cannot be None")
    
    first_day_of_next_month = datetime.date(target_date.year, target_date.month + 1, 1) if target_date.month < 12 else datetime.date(target_date.year + 1, 1, 1)
    last_day_of_current_month = first_day_of_next_month - datetime.timedelta(days=1)
    
    days_remaining = (last_day_of_current_month - target_date).days
    
    return days_remaining

if __name__ == '__main__':
    sample_dates = [
        datetime.date(2023, 10, 15),
        datetime.date(2023, 2, 28),
        datetime.date(2024, 2, 29),
        datetime.date(2023, 12, 31)
    ]
    
    for date in sample_dates:
        result = calculate_days_remaining_in_month(date)
        print(result)