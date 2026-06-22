from datetime import datetime
from typing import Tuple

def validate_datetime_inputs(dt1: datetime, dt2: datetime) -> Tuple[datetime, datetime]:
    if not isinstance(dt1, datetime):
        raise ValueError("First argument must be a datetime instance")
    if not isinstance(dt2, datetime):
        raise ValueError("Second argument must be a datetime instance")
    return dt1, dt2

def calculate_precise_year_difference(dt1: datetime, dt2: datetime) -> float:
    dt1, dt2 = validate_datetime_inputs(dt1, dt2)
    
    if dt1 > dt2:
        dt1, dt2 = dt2, dt1
        
    delta = dt2 - dt1
    total_days = delta.days
    total_seconds = delta.seconds
    
    decimal_days = total_days + (total_seconds / 86400)
    
    years = 0
    current_date = dt1
    while True:
        try:
            next_year_date = current_date.replace(year=current_date.year + 1)
        except ValueError:
            next_year_date = current_date.replace(year=current_date.year + 1, day=28)
            
        days_in_year = (next_year_date - current_date).days
        
        if decimal_days >= days_in_year:
            years += 1
            decimal_days -= days_in_year
            current_date = next_year_date
        else:
            break
            
    fraction = decimal_days / 365.2425
    return years + fraction

if __name__ == '__main__':
    start_dt = datetime(2015, 6, 15, 10, 30, 0)
    end_dt = datetime(2023, 12, 25, 14, 45, 0)
    diff = calculate_precise_year_difference(start_dt, end_dt)
    print(diff)