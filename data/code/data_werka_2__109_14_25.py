import datetime
import calendar

def get_remaining_month_duration(reference_date: datetime.date) -> dict:
    year = reference_date.year
    month = reference_date.month
    
    if month == 12:
        next_month_start = datetime.date(year + 1, 1, 1)
    else:
        next_month_start = datetime.date(year, month + 1, 1)
    
    last_day_of_month = calendar.monthrange(year, month)[1]
    current_month_end = datetime.date(year, month, last_day_of_month)
    
    remaining_days = (next_month_start - reference_date).days
    
    hours = 24 - reference_date.hour
    minutes = 60 - reference_date.minute
    seconds = 60 - reference_date.second
    
    if seconds == 60:
        seconds = 0
        minutes -= 1
    
    if minutes == 60:
        minutes = 0
        hours -= 1
    
    if hours == 24:
        hours = 0
        remaining_days -= 1
    
    if remaining_days < 0:
        remaining_days = 0
        hours = 0
        minutes = 0
        seconds = 0
    
    return {
        "days": remaining_days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    sample_time = datetime.time(14, 30, 45)
    reference_datetime = datetime.datetime.combine(sample_date, sample_time)
    
    result = get_remaining_month_duration(reference_datetime.date())
    
    print(result)