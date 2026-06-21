import datetime

def count_weekdays_left_in_month(reference_date: datetime.date) -> int:
    today = reference_date
    year = today.year
    month = today.month
    
    if month == 12:
        next_month_start = datetime.date(year + 1, 1, 1)
    else:
        next_month_start = datetime.date(year, month + 1, 1)
    
    last_day_of_month = next_month_start - datetime.timedelta(days=1)
    
    days_left = (last_day_of_month - today).days + 1
    
    weekdays_count = 0
    current_date = today
    while current_date <= last_day_of_month:
        if current_date.weekday() < 5:
            weekdays_count += 1
        current_date += datetime.timedelta(days=1)
        
    return weekdays_count

if __name__ == '__main__':
    ref_date = datetime.date(2023, 10, 15)
    result = count_weekdays_left_in_month(ref_date)
    print(result)