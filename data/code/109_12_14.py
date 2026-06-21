import datetime
import calendar

def get_month_progress(year: int, month: int) -> dict:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    
    first_day = datetime.date(year, month, 1)
    last_day = datetime.date(year, month, calendar.monthrange(year, month)[1])
    
    today = datetime.date.today()
    
    if today < first_day:
        total_days = (last_day - first_day).days + 1
        remaining_days = total_days
        completed_days = 0
    elif today > last_day:
        total_days = (last_day - first_day).days + 1
        remaining_days = 0
        completed_days = total_days
    else:
        total_days = (last_day - first_day).days + 1
        completed_days = (today - first_day).days + 1
        remaining_days = total_days - completed_days
    
    percentage = (completed_days / total_days) * 100 if total_days > 0 else 0.0
    
    return {
        "year": year,
        "month": month,
        "total_days": total_days,
        "completed_days": completed_days,
        "remaining_days": remaining_days,
        "percentage": percentage
    }

if __name__ == '__main__':
    result = get_month_progress(2023, 10)
    print(result)