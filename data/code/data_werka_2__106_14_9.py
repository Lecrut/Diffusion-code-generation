from datetime import datetime

def calculate_year_span(reference_date: datetime, target_date: datetime) -> int:
    if not isinstance(reference_date, datetime):
        raise ValueError("reference_date must be a datetime instance")
    if not isinstance(target_date, datetime):
        raise ValueError("target_date must be a datetime instance")
    
    year1 = reference_date.year
    year2 = target_date.year
    
    if year1 == year2:
        return 0
    
    month1 = reference_date.month
    day1 = reference_date.day
    month2 = target_date.month
    day2 = target_date.day
    
    is_complete_year_passed = (month2 > month1) or (month2 == month1 and day2 >= day1)
    
    raw_diff = abs(year1 - year2)
    
    if raw_diff == 1:
        return 1
    
    if is_complete_year_passed:
        return raw_diff
    
    return raw_diff - 1

if __name__ == '__main__':
    start_dt = datetime(2015, 3, 10)
    end_dt = datetime(2020, 11, 15)
    span = calculate_year_span(start_dt, end_dt)
    print(span)