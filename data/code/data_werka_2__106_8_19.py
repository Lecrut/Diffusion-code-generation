from datetime import datetime
from typing import Tuple

def calculate_year_difference(dt1: datetime, dt2: datetime) -> int:
    if not isinstance(dt1, datetime) or not isinstance(dt2, datetime):
        raise ValueError("Both arguments must be datetime instances")
    
    def get_year_span(start: datetime, end: datetime) -> int:
        if start > end:
            return get_year_span(end, start)
        
        year_diff = end.year - start.year
        
        if end.month < start.month:
            return year_diff - 1
        if end.month == start.month and end.day < start.day:
            return year_diff - 1
        
        return year_diff

    return get_year_span(dt1, dt2)

if __name__ == '__main__':
    start_date = datetime(2015, 8, 12)
    end_date = datetime(2024, 3, 5)
    diff = calculate_year_difference(start_date, end_date)
    print(diff)