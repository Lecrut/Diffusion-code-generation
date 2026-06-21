import threading
import time
from datetime import datetime, timedelta

_lock = threading.Lock()
_cache = {"value": None, "timestamp": 0.0}

def get_elapsed_time_from_midnight() -> float:
    with _lock:
        now = time.time()
        if _cache["value"] is not None and (now - _cache["timestamp"]) < 1.0:
            return _cache["value"]
        current_datetime = datetime.now()
        midnight_today = current_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
        elapsed = (current_datetime - midnight_today).total_seconds()
        _cache["value"] = elapsed
        _cache["timestamp"] = now
        return elapsed

if __name__ == "__main__":
    result = get_elapsed_time_from_midnight()
    print(result)