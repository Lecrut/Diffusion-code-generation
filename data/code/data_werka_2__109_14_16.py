import datetime
import calendar

def get_remaining_month_duration(reference_date: datetime.date) -> dict:
    year = reference_date.year
    month = reference_date.month
    
    if month == 12:
        next_month_start = datetime.date(year + 1, 1, 1)
    else:
        next_month_start = datetime.date(year, month + 1, 1)
    
    last_day_of_current_month = calendar.monthrange(year, month)[1]
    current_month_end = datetime.date(year, month, last_day_of_current_month)
    
    days_remaining = (next_month_start - reference_date).days
    
    hours_remaining = 24 - reference_date.hour
    minutes_remaining = 60 - reference_date.minute
    seconds_remaining = 60 - reference_date.second
    
    if seconds_remaining == 60:
        seconds_remaining = 0
        minutes_remaining -= 1
    
    if minutes_remaining == 60:
        minutes_remaining = 0
        hours_remaining -= 1
    
    if hours_remaining == 24:
        hours_remaining = 0
        days_remaining -= 1
    
    if days_remaining < 0:
        days_remaining = 0
        hours_remaining = 0
        minutes_remaining = 0
        seconds_remaining = 0
        
    return {
        "days": days_remaining,
        "hours": hours_remaining,
        "minutes": minutes_remaining,
        "seconds": seconds_remaining
    }

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    sample_time = datetime.time(14, 30, 45)
    reference_datetime = datetime.datetime.combine(sample_date, sample_time)
    
    result = get_remaining_month_duration(reference_datetime)
    
    print(result)