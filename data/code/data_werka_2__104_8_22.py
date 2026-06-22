from datetime import datetime
from dateutil.relativedelta import relativedelta

def is_within_one_week(date1: datetime, date2: datetime) -> bool:
    delta = relativedelta(date1, date2)
    days_diff = abs(delta.days)
    if delta.days < 0:
        days_diff = 7 - delta.days
    else:
        days_diff = delta.days
    
    if delta.weeks > 0:
        return False
    
    return days_diff <= 7

if __name__ == '__main__':
    date1 = datetime(2023, 10, 1)
    date2 = datetime(2023, 10, 8)
    result = is_within_one_week(date1, date2)
    print(result)