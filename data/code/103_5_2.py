import threading
import time
from datetime import timedelta

_lock = threading.RLock()
SECONDS_IN_DAY = 86400

def compute_seconds_since_midnight(reference_time: float | None = None) -> float:
    if reference_time is None:
        reference_time = time.time()
    with _lock:
        current_datetime = time.gmtime(reference_time)
        seconds_in_current_day = (
            current_datetime.tm_hour * 3600
            + current_datetime.tm_min * 60
            + current_datetime.tm_sec
        )
        return float(seconds_in_current_day)

def main() -> None:
    sample_reference = 1609459200.0
    elapsed = compute_seconds_since_midnight(sample_reference)
    print(elapsed)

if __name__ == '__main__':
    main()