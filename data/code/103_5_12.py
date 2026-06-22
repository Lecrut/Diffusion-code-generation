import threading
from datetime import datetime, time, timedelta

_UNITS = {
    "seconds": 1,
    "minutes": 60,
    "hours": 3600,
}

_lock = threading.Lock()

def get_elapsed_seconds_from_midnight(unit: str = "seconds") -> float:
    with _lock:
        now = datetime.now()
        midnight = datetime.combine(now.date(), time.min)
        delta = now - midnight
        total_seconds = delta.total_seconds()
        multiplier = _UNITS[unit]
        return total_seconds / multiplier

def main() -> None:
    sample_unit = "minutes"
    result = get_elapsed_seconds_from_midnight(sample_unit)
    print(result)

if __name__ == "__main__":
    main()