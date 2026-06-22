import threading
from datetime import datetime, time, timedelta

_lock = threading.Lock()
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def calculate_seconds_since_midnight(reference_dt: datetime | None = None) -> float:
    if reference_dt is None:
        reference_dt = datetime.now()
    with _lock:
        today = reference_dt.date()
        midnight = datetime.combine(today, time.min)
        elapsed = reference_dt - midnight
        total_seconds = elapsed.total_seconds()
        return total_seconds

def main() -> None:
    sample_dt = datetime(2023, 10, 25, 14, 30, 45)
    seconds = calculate_seconds_since_midnight(sample_dt)
    print(seconds)

if __name__ == '__main__':
    main()