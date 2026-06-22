import datetime

def count_weekdays_left_in_month(reference_date=None):
    if reference_date is None:
        reference_date = datetime.date.today()
    
    year = reference_date.year
    month = reference_date.month
    day = reference_date.day
    
    first_day_of_month = datetime.date(year, month, 1)
    last_day_of_month = datetime.date(year, month, 1)
    
    if month == 12:
        next_month = datetime.date(year + 1, 1, 1)
    else:
        next_month = datetime.date(year, month + 1, 1)
    
    last_day_of_month = next_month - datetime.timedelta(days=1)
    
    days_left = (last_day_of_month - reference_date).days
    
    if days_left < 0:
        return 0
    
    total_days = days_left + 1
    
    start_weekday = reference_date.weekday()
    
    full_weeks = total_days // 7
    remaining_days = total_days % 7
    
    weekdays_in_full_weeks = full_weeks * 5
    
    weekdays_in_remaining = 0
    for i in range(remaining_days):
        current_weekday = (start_weekday + i) % 7
        if current_weekday < 5:
            weekdays_in_remaining += 1
            
    return weekdays_in_full_weeks + weekdays_in_remaining

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    result = count_weekdays_left_in_month(sample_date)
    print(result)