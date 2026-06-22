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
    
    remaining_days = (current_month_end - reference_date).days
    
    remaining_seconds = 0
    if remaining_days > 0:
        remaining_seconds = (next_month_start - current_month_end).total_seconds()
        remaining_seconds += (24 * 3600 * remaining_days)
    else:
        remaining_seconds = (next_month_start - reference_date).total_seconds()
    
    total_seconds = int(remaining_seconds)
    
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
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