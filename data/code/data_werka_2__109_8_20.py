import datetime

def count_weekdays_left_in_month(reference_date: datetime.date) -> int:
    if not isinstance(reference_date, datetime.date):
        raise ValueError("reference_date must be a datetime.date instance")
    
    year = reference_date.year
    month = reference_date.month
    
    first_day = datetime.date(year, month, 1)
    last_day = datetime.date(year, month, 1)
    
    if month == 12:
        last_day = datetime.date(year, 12, 31)
    else:
        next_month = datetime.date(year, month + 1, 1)
        last_day = next_month - datetime.timedelta(days=1)
    
    today = reference_date
    
    if today > last_day:
        return 0
    
    weekdays_count = 0
    current = first_day
    
    while current <= last_day:
        if current.weekday() < 5:
            if current >= today:
                weekdays_count += 1
        current += datetime.timedelta(days=1)
    
    return weekdays_count

if __name__ == '__main__':
    ref_date = datetime.date(2023, 10, 15)
    result = count_weekdays_left_in_month(ref_date)
    print(result)