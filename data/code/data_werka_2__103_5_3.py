import threading
from datetime import datetime, time

_lock = threading.Lock()

def get_elapsed_seconds_from_midnight() -> float:
    with _lock:
        now = datetime.now()
        midnight_today = datetime.combine(now.date(), time.min)
        delta = now - midnight_today
        return delta.total_seconds()

if __name__ == '__main__':
    result = get_elapsed_seconds_from_midnight()
    print(result)