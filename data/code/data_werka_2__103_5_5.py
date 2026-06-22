import threading
import time
from datetime import datetime, timedelta

_lock = threading.Lock()
_cache = {}

def _get_midnight_today():
    now = datetime.now()
    return now.replace(hour=0, minute=0, second=0, microsecond=0)

def get_elapsed_seconds_from_midnight():
    with _lock:
        midnight = _get_midnight_today()
        now = datetime.now()
        delta = now - midnight
        return delta.total_seconds()

if __name__ == '__main__':
    result = get_elapsed_seconds_from_midnight()
    print(result)