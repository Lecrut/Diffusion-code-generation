import threading
from datetime import datetime, time as dt_time
from dataclasses import dataclass

@dataclass
class TimeTracker:
    _lock: threading.Lock
    _last_midnight: float
    _last_midnight_dt: datetime

    def __init__(self) -> None:
        self._lock = threading.Lock()
        now = datetime.now()
        midnight = datetime.combine(now.date(), dt_time.min)
        self._last_midnight = midnight.timestamp()
        self._last_midnight_dt = midnight

    def get_elapsed_seconds(self) -> float:
        with self._lock:
            now = datetime.now()
            current_midnight = datetime.combine(now.date(), dt_time.min)
            if current_midnight != self._last_midnight_dt:
                self._last_midnight = current_midnight.timestamp()
                self._last_midnight_dt = current_midnight
            return now.timestamp() - self._last_midnight

    def get_current_time(self) -> str:
        with self._lock:
            return datetime.now().strftime("%H:%M:%S")

def main() -> None:
    tracker = TimeTracker()
    elapsed = tracker.get_elapsed_seconds()
    current = tracker.get_current_time()
    print(elapsed)
    print(current)

if __name__ == '__main__':
    main()