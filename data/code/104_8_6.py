from datetime import datetime
from dateutil.relativedelta import relativedelta

def is_within_one_week(date1: datetime, date2: datetime) -> bool:
    delta = relativedelta(date1, date2)
    abs_days = abs(delta.days)
    abs_months = abs(delta.months)
    abs_years = abs(delta.years)
    
    if abs_years > 0:
        return False
    if abs_months > 0:
        return False
    return abs_days <= 7

if __name__ == '__main__':
    date1 = datetime(2023, 10, 1, 12, 0, 0)
    date2 = datetime(2023, 10, 8, 12, 0, 0)
    result = is_within_one_week(date1, date2)
    print(result)