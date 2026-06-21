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
        last_day_of_month = datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
    else:
        last_day_of_month = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
    
    current_date = reference_date
    weekdays_count = 0
    
    while current_date <= last_day_of_month:
        if current_date.weekday() < 5:
            weekdays_count += 1
        current_date += datetime.timedelta(days=1)
    
    return weekdays_count

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    result = count_weekdays_left_in_month(sample_date)
    print(result)