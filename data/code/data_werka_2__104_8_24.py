from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse

def is_within_one_week(date1_str: str, date2_str: str) -> bool:
    date1 = parse(date1_str)
    date2 = parse(date2_str)
    
    if not isinstance(date1, datetime):
        raise ValueError("date1 is not a valid datetime")
    if not isinstance(date2, datetime):
        raise ValueError("date2 is not a valid datetime")
        
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
    d1 = "2023-10-15 10:30:00"
    d2 = "2023-10-22 10:30:00"
    result = is_within_one_week(d1, d2)
    print(result)