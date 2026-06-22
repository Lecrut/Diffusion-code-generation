import datetime

def weekdays_left_in_month(reference_date: datetime.date) -> int:
    today = reference_date
    year = today.year
    month = today.month
    
    if month == 12:
        next_month = datetime.date(year + 1, 1, 1)
    else:
        next_month = datetime.date(year, month + 1, 1)
    
    last_day_of_month = next_month - datetime.timedelta(days=1)
    
    current = today
    count = 0
    
    while current <= last_day_of_month:
        if current.weekday() < 5:
            count += 1
        current += datetime.timedelta(days=1)
        
    return count

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    result = weekdays_left_in_month(sample_date)
    print(result)