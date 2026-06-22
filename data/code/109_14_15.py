import datetime

def get_remaining_month_duration(reference_date: datetime.date) -> dict:
    year = reference_date.year
    month = reference_date.month
    
    if month == 12:
        next_month_start = datetime.date(year + 1, 1, 1)
    else:
        next_month_start = datetime.date(year, month + 1, 1)
    
    last_day_of_month = next_month_start - datetime.timedelta(days=1)
    last_day_of_month_time = datetime.datetime.combine(last_day_of_month, datetime.time(23, 59, 59))
    
    now = datetime.datetime.now()
    reference_datetime = datetime.datetime.combine(reference_date, datetime.time(0, 0, 0))
    
    if now > last_day_of_month_time:
        remaining_seconds = 0
    elif now < reference_datetime:
        delta = last_day_of_month_time - reference_datetime
        remaining_seconds = int(delta.total_seconds())
    else:
        delta = last_day_of_month_time - now
        remaining_seconds = int(delta.total_seconds())
    
    days = remaining_seconds // 86400
    hours = (remaining_seconds % 86400) // 3600
    minutes = (remaining_seconds % 3600) // 60
    seconds = remaining_seconds % 60
    
    return {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    result = get_remaining_month_duration(sample_date)
    print(result)