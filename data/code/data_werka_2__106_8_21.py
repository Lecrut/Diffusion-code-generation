from datetime import datetime
from typing import Tuple

def calculate_year_difference(start: datetime, end: datetime) -> int:
    if not isinstance(start, datetime):
        raise ValueError("start must be a datetime instance")
    if not isinstance(end, datetime):
        raise ValueError("end must be a datetime instance")
    
    start_date = start.date()
    end_date = end.date()
    
    years = end_date.year - start_date.year
    
    if (end_date.month, end_date.day) < (start_date.month, start_date.day):
        years -= 1
        
    return years

if __name__ == '__main__':
    start_date = datetime(2015, 11, 12)
    end_date = datetime(2023, 10, 11)
    result = calculate_year_difference(start_date, end_date)
    print(result)