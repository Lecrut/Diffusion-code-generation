import threading
import time
from datetime import datetime, timedelta

_lock = threading.Lock()
_cache = {}

def get_elapsed_seconds_from_midnight() -> float:
    with _lock:
        today = datetime.now().date()
        if today in _cache:
            return _cache[today]
        now = datetime.now()
        midnight = datetime.combine(today, datetime.min.time())
        elapsed = (now - midnight).total_seconds()
        _cache[today] = elapsed
        return elapsed

if __name__ == '__main__':
    result = get_elapsed_seconds_from_midnight()
    print(result)