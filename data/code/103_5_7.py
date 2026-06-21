import threading
from datetime import datetime, time
from time import time as current_time

_lock = threading.Lock()
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def calculate_seconds_since_midnight_utc() -> float:
    with _lock:
        now = datetime.utcnow()
        midnight = datetime.combine(now.date(), time.min)
        delta_seconds = (now - midnight).total_seconds()
        return float(delta_seconds)

def main() -> None:
    sample_timestamp = 1672531200.0
    elapsed = calculate_seconds_since_midnight_utc()
    print(elapsed)

if __name__ == '__main__':
    main()