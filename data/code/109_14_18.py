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
    
    remaining_seconds = int((next_month_start - reference_date).total_seconds())
    
    days = remaining_seconds // 86400
    remaining_seconds %= 86400
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    return {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15, 10, 30, 45)
    result = get_remaining_month_duration(sample_date)
    print(result)