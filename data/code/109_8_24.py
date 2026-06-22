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
    
    total_days_in_month = (last_day_of_month - first_day_of_month).days + 1
    
    days_passed = day
    days_left = total_days_in_month - days_passed
    
    if days_left <= 0:
        return 0
    
    start_date = reference_date
    end_date = last_day_of_month
    
    weekdays_count = 0
    current_date = start_date
    
    while current_date <= end_date:
        if current_date.weekday() < 5:
            weekdays_count += 1
        current_date += datetime.timedelta(days=1)
    
    return weekdays_count

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    result = count_weekdays_left_in_month(sample_date)
    print(result)