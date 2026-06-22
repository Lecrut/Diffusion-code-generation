import calendar
import datetime

_MONTH_DAYS = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}

def get_remaining_hours_in_month(date_obj: datetime.datetime) -> float:
    if date_obj.tzinfo is not None:
        raise ValueError("Timezone-aware dates are not supported for this calculation.")
    
    year = date_obj.year
    month = date_obj.month
    
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    if month == 2 and is_leap:
        days_in_month = 29
    else:
        days_in_month = _MONTH_DAYS.get(month, 31)
        
    target_date = date_obj.replace(hour=23, minute=59, second=59, microsecond=999999)
    delta = target_date - date_obj
    
    total_seconds = delta.total_seconds()
    
    if total_seconds < 0:
        return 0.0
        
    return total_seconds / 3600.0

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 15, 14, 30, 0)
    hours_remaining = get_remaining_hours_in_month(sample_date)
    print(hours_remaining)