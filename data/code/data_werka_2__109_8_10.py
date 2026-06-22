import datetime

def count_weekdays_left_in_month(reference_date: datetime.date) -> int:
    today = reference_date
    year = today.year
    month = today.month
    
    if month == 12:
        next_month_year = year + 1
        next_month_month = 1
    else:
        next_month_year = year
        next_month_month = month + 1
    
    last_day_of_month = datetime.date(next_month_year, next_month_month, 1) - datetime.timedelta(days=1)
    
    days_left = (last_day_of_month - today).days + 1
    
    weekdays = 0
    for i in range(days_left):
        current_day = today + datetime.timedelta(days=i)
        if current_day.weekday() < 5:
            weekdays += 1
            
    return weekdays

if __name__ == '__main__':
    ref_date = datetime.date(2023, 10, 15)
    result = count_weekdays_left_in_month(ref_date)
    print(result)