import threading
from datetime import datetime, time as dt_time, timedelta
from typing import Optional

SECONDS_IN_MINUTE = 60
MILLISECONDS_IN_SECOND = 1000

_lock = threading.Lock()

def calculate_elapsed_seconds_from_midnight(reference_dt: Optional[datetime] = None) -> float:
    if reference_dt is None:
        reference_dt = datetime.now()
    else:
        reference_dt = reference_dt.replace(microsecond=0)
    
    midnight_today = datetime.combine(reference_dt.date(), dt_time.min)
    delta = reference_dt - midnight_today
    
    total_seconds = delta.total_seconds()
    return total_seconds

if __name__ == '__main__':
    sample_time = datetime(2023, 10, 27, 12, 30, 45)
    result = calculate_elapsed_seconds_from_midnight(sample_time)
    print(result)