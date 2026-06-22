from datetime import datetime
from dateutil.relativedelta import relativedelta

def check_week_proximity(reference_date: datetime, target_date: datetime) -> bool:
    if not isinstance(reference_date, datetime):
        raise ValueError("reference_date must be a datetime object")
    if not isinstance(target_date, datetime):
        raise ValueError("target_date must be a datetime object")
    
    delta = relativedelta(target_date, reference_date)
    
    total_days = delta.days
    if delta.months > 0:
        total_days += 30 * delta.months
    if delta.years > 0:
        total_days += 365 * delta.years
        
    if delta.hours > 0 or delta.minutes > 0 or delta.seconds > 0:
        total_days += 1
        
    return abs(total_days) <= 7

if __name__ == '__main__':
    date_a = datetime(2023, 11, 1, 10, 30, 0)
    date_b = datetime(2023, 11, 7, 10, 30, 0)
    is_close = check_week_proximity(date_a, date_b)
    print(is_close)