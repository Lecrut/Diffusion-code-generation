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
    
    remaining_days = (next_month_start - reference_date).days
    
    hours_in_current_day = 24 - reference_date.hour
    minutes_in_current_hour = 60 - reference_date.minute
    seconds_in_current_minute = 60 - reference_date.second
    
    if seconds_in_current_minute == 60:
        seconds_in_current_minute = 0
        minutes_in_current_hour -= 1
    
    if minutes_in_current_hour == 60:
        minutes_in_current_hour = 0
        hours_in_current_day -= 1
    
    if hours_in_current_day == 24:
        hours_in_current_day = 0
        remaining_days -= 1
    
    total_seconds = (remaining_days * 24 * 3600) + (hours_in_current_day * 3600) + (minutes_in_current_hour * 60) + seconds_in_current_minute
    
    days = total_seconds // 86400
    remainder = total_seconds % 86400
    hours = remainder // 3600
    remainder = remainder % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    
    return {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 15, 14, 30, 45)
    result = get_remaining_month_duration(sample_date)
    print(result)