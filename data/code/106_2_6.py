from datetime import datetime

def calculate_year_difference(start_date: datetime, end_date: datetime) -> int:
    if not isinstance(start_date, datetime):
        raise ValueError("start_date must be a datetime instance")
    if not isinstance(end_date, datetime):
        raise ValueError("end_date must be a datetime instance")
    if end_date < start_date:
        raise ValueError("end_date must be greater than or equal to start_date")
    
    year_diff = end_date.year - start_date.year
    
    if year_diff == 0:
        return 0
    
    start_anniversary = start_date.replace(year=end_date.year)
    
    if end_date < start_anniversary:
        return year_diff - 1
    
    return year_diff

if __name__ == '__main__':
    start_dt = datetime(2010, 5, 15)
    end_dt = datetime(2023, 5, 14)
    diff = calculate_year_difference(start_dt, end_dt)
    print(diff)