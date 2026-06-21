from datetime import datetime
import calendar

def get_year_difference(start: datetime, end: datetime) -> int:
    if not isinstance(start, datetime):
        raise ValueError("start must be a datetime object")
    if not isinstance(end, datetime):
        raise ValueError("end must be a datetime object")
    if end < start:
        raise ValueError("end must be greater than or equal to start")
    
    year_diff = end.year - start.year
    
    if year_diff == 0:
        return 0
    
    start_month_day = (start.month, start.day)
    end_month_day = (end.month, end.day)
    
    if end_month_day < start_month_day:
        return year_diff - 1
    
    return year_diff

if __name__ == '__main__':
    date_start = datetime(2010, 5, 15)
    date_end = datetime(2023, 5, 14)
    difference = get_year_difference(date_start, date_end)
    print(difference)