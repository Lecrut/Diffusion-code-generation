from datetime import datetime, timedelta

def get_remaining_month_duration(reference_date: datetime) -> dict:
    year = reference_date.year
    month = reference_date.month
    
    if month == 12:
        next_month_start = datetime(year + 1, 1, 1)
    else:
        next_month_start = datetime(year, month + 1, 1)
    
    remaining_seconds = int((next_month_start - reference_date).total_seconds())
    
    if remaining_seconds < 0:
        raise ValueError("Reference date is after the start of the next month")
    
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
    sample_date = datetime(2023, 10, 15, 10, 30, 45)
    result = get_remaining_month_duration(sample_date)
    print(result)