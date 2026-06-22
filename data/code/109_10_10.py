import datetime

def days_remaining_in_month(year, month):
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    
    if month == 12:
        next_month_first_day = datetime.date(year + 1, 1, 1)
    else:
        next_month_first_day = datetime.date(year, month + 1, 1)
    
    last_day_of_month = next_month_first_day - datetime.timedelta(days=1)
    
    today = datetime.date.today()
    
    if today.year == year and today.month == month:
        return (last_day_of_month - today).days
    else:
        return (last_day_of_month - datetime.date(year, month, 1)).days + 1

if __name__ == '__main__':
    current_year = datetime.date.today().year
    current_month = datetime.date.today().month
    
    remaining_days = days_remaining_in_month(current_year, current_month)
    print(remaining_days)
    
    sample_year = 2023
    sample_month = 2
    sample_remaining = days_remaining_in_month(sample_year, sample_month)
    print(sample_remaining)