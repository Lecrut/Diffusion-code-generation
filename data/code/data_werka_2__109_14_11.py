from datetime import datetime, timedelta

def get_remaining_month_duration(reference_date: datetime) -> dict:
    if reference_date.month == 12:
        next_month_start = datetime(reference_date.year + 1, 1, 1)
    else:
        next_month_start = datetime(reference_date.year, reference_date.month + 1, 1)
    
    remaining_seconds = (next_month_start - reference_date).total_seconds()
    
    if remaining_seconds < 0:
        raise ValueError("Reference date must be before the start of the next month")
    
    days = int(remaining_seconds // 86400)
    remaining_seconds %= 86400
    hours = int(remaining_seconds // 3600)
    remaining_seconds %= 3600
    minutes = int(remaining_seconds // 60)
    seconds = int(remaining_seconds % 60)
    
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