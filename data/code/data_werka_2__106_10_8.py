from datetime import datetime
import calendar

def get_year_difference(start: datetime, end: datetime) -> int:
    if start == end:
        return 0
    
    if start > end:
        start, end = end, start
    
    year_diff = end.year - start.year
    
    if year_diff == 0:
        return 0
    
    start_month_day = (start.month, start.day)
    end_month_day = (end.month, end.day)
    
    if end_month_day < start_month_day:
        year_diff -= 1
    
    return abs(year_diff)

if __name__ == '__main__':
    d1 = datetime(2000, 2, 29)
    d2 = datetime(2021, 2, 28)
    diff = get_year_difference(d1, d2)
    print(diff)