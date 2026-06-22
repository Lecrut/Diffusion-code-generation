import datetime

def get_remaining_month_duration(reference_date: datetime.date) -> dict:
    year = reference_date.year
    month = reference_date.month
    
    if month == 12:
        next_month_start = datetime.date(year + 1, 1, 1)
    else:
        next_month_start = datetime.date(year, month + 1, 1)
    
    days_in_current_month = (next_month_start - reference_date).days
    
    now = datetime.datetime.now()
    if now.date() != reference_date:
        raise ValueError("Reference date must be today's date to calculate remaining duration accurately.")
    
    remaining_seconds = (next_month_start - now).total_seconds()
    
    if remaining_seconds < 0:
        remaining_seconds = 0
    
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
    today = datetime.date.today()
    result = get_remaining_month_duration(today)
    print(result)