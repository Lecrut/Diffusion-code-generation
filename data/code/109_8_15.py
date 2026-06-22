import datetime

def count_weekdays_left_in_month(reference_date: datetime.date = None) -> int:
    if reference_date is None:
        reference_date = datetime.date.today()
    
    year = reference_date.year
    month = reference_date.month
    
    first_day_of_month = datetime.date(year, month, 1)
    last_day_of_month = datetime.date(year, month, 28) + datetime.timedelta(days=4)
    last_day_of_month = last_day_of_month.replace(day=1) - datetime.timedelta(days=1)
    
    today = reference_date
    if today > last_day_of_month:
        return 0
    
    weekdays_count = 0
    current_day = today
    
    while current_day <= last_day_of_month:
        if current_day.weekday() < 5:
            weekdays_count += 1
        current_day += datetime.timedelta(days=1)
        
    return weekdays_count

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    result = count_weekdays_left_in_month(sample_date)
    print(result)