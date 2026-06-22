import datetime

def count_weekdays_left_in_month(reference_date: datetime.date) -> int:
    today = datetime.date.today()
    year = reference_date.year
    month = reference_date.month
    
    if month == 12:
        next_month_start = datetime.date(year + 1, 1, 1)
    else:
        next_month_start = datetime.date(year, month + 1, 1)
    
    last_day_of_month = next_month_start - datetime.timedelta(days=1)
    
    start_date = max(today, reference_date)
    
    if start_date > last_day_of_month:
        return 0
    
    count = 0
    current = start_date
    while current <= last_day_of_month:
        if current.weekday() < 5:
            count += 1
        current += datetime.timedelta(days=1)
    
    return count

if __name__ == '__main__':
    ref_date = datetime.date(2023, 10, 15)
    result = count_weekdays_left_in_month(ref_date)
    print(result)