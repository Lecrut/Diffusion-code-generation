import datetime

def days_remaining_in_month(year, month):
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    
    if month == 12:
        next_month = datetime.date(year + 1, 1, 1)
    else:
        next_month = datetime.date(year, month + 1, 1)
    
    first_day_of_next_month = next_month
    last_day_of_current_month = first_day_of_next_month - datetime.timedelta(days=1)
    
    today = datetime.date(year, month, 1)
    days_passed = (today - today.replace(day=1)).days + 1
    
    total_days_in_month = last_day_of_next_month.day - 1
    remaining_days = total_days_in_month - days_passed + 1
    
    return remaining_days

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    result = days_remaining_in_month(sample_year, sample_month)
    print(result)