from datetime import datetime, timedelta
from typing import Union

def compute_timedelta(start: datetime, end: datetime) -> Union[timedelta, float]:
    if not isinstance(start, datetime) or not isinstance(end, datetime):
        raise ValueError("Inputs must be datetime objects")
    
    delta = end - start
    total_seconds = delta.total_seconds()
    
    if total_seconds < 0:
        positive_seconds = abs(total_seconds)
        return positive_seconds
    
    return delta

if __name__ == '__main__':
    dt_start = datetime(2023, 5, 15, 8, 30, 0)
    dt_end = datetime(2023, 5, 15, 10, 45, 30)
    
    result = compute_timedelta(dt_start, dt_end)
    print(result)