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
    
    last_day_of_month = next_month_start - datetime.timedelta(days=1)
    today = datetime.date(year, month, 1)
    
    days_in_month = last_day_of_month.day
    
    sample_day = 15
    if sample_day > days_in_month:
        sample_day = days_in_month
        
    current_date = datetime.date(year, month, sample_day)
    remaining_days = (last_day_of_month - current_date).days
    
    return remaining_days

if __name__ == '__main__':
    result = days_remaining_in_month(2023, 10)
    print(result)