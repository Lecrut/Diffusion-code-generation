import threading
import time
from datetime import datetime, time as dt_time

_lock = threading.Lock()

def get_elapsed_seconds_from_midnight() -> float:
    with _lock:
        now = datetime.now()
        midnight = datetime.combine(now.date(), dt_time.min)
        delta = now - midnight
        return delta.total_seconds()

if __name__ == '__main__':
    result = get_elapsed_seconds_from_midnight()
    print(result)