import threading
from datetime import datetime, time

_lock = threading.Lock()
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def calculate_seconds_since_midnight() -> float:
    with _lock:
        now = datetime.now()
        current_time = now.time()
        hours = current_time.hour
        minutes = current_time.minute
        seconds = current_time.second
        microseconds = current_time.microsecond
        total_seconds = hours * SECONDS_PER_HOUR + minutes * SECONDS_PER_MINUTE + seconds
        fractional_seconds = microseconds / 1000000.0
        return total_seconds + fractional_seconds

if __name__ == '__main__':
    result = calculate_seconds_since_midnight()
    print(result)