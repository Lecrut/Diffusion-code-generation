from datetime import datetime, timedelta
import math

class TimeDeltaResult:
    def __init__(self, delta: timedelta, total_seconds: float):
        self.delta = delta
        self.total_seconds = total_seconds

def compute_signed_difference(start: datetime, end: datetime) -> TimeDeltaResult:
    if not isinstance(start, datetime):
        raise ValueError("start must be a datetime instance")
    if not isinstance(end, datetime):
        raise ValueError("end must be a datetime instance")
    
    delta = end - start
    total_seconds = delta.total_seconds()
    
    return TimeDeltaResult(delta, total_seconds)

if __name__ == '__main__':
    t1 = datetime(2024, 5, 1, 14, 30, 0)
    t2 = datetime(2024, 5, 1, 12, 15, 0)
    
    res = compute_signed_difference(t1, t2)
    print(res.delta)
    print(res.total_seconds)