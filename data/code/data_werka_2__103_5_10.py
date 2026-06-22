import threading
import time
from datetime import datetime, timedelta

_lock = threading.Lock()

def get_elapsed_seconds_from_midnight() -> float:
    with _lock:
        now = datetime.now()
        midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
        delta = now - midnight
        return delta.total_seconds()

if __name__ == '__main__':
    result = get_elapsed_seconds_from_midnight()
    print(result)