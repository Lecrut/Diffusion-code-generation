from datetime import datetime
from dateutil.relativedelta import relativedelta

def is_within_one_week(date1: datetime, date2: datetime) -> bool:
    delta = relativedelta(date1, date2)
    days_diff = abs(delta.days)
    if delta.days < 0:
        days_diff = 7 - delta.days if delta.days == -1 else abs(delta.days)
    else:
        days_diff = delta.days
    
    if delta.days < 0:
        total_days = abs(delta.days)
        if delta.hours > 0 or delta.minutes > 0 or delta.seconds > 0:
            total_days += 1
    else:
        total_days = delta.days
        if delta.hours > 0 or delta.minutes > 0 or delta.seconds > 0:
            total_days += 1
            
    return total_days <= 7

if __name__ == '__main__':
    date1 = datetime(2023, 10, 1, 12, 0, 0)
    date2 = datetime(2023, 10, 8, 12, 0, 0)
    result = is_within_one_week(date1, date2)
    print(result)