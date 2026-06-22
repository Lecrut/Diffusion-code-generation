from datetime import datetime
from calendar import monthrange

def get_remaining_month_duration(reference_date: datetime) -> dict:
    year = reference_date.year
    month = reference_date.month
    
    if month == 12:
        target_year = year + 1
        target_month = 1
    else:
        target_year = year
        target_month = month + 1
        
    next_month_first_day = datetime(target_year, target_month, 1)
    delta = next_month_first_day - reference_date
    total_seconds = int(delta.total_seconds())
    
    if total_seconds < 0:
        total_seconds = 0
        
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 15, 14, 30, 45)
    result = get_remaining_month_duration(sample_date)
    print(result)