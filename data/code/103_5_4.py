import threading
from datetime import datetime, time
import math

class TimeCalculator:
    def __init__(self):
        self._lock = threading.Lock()
        self._last_computed = 0.0
        self._last_timestamp = 0.0

    def get_elapsed_from_midnight(self) -> float:
        with self._lock:
            now = datetime.now()
            midnight = datetime.combine(now.date(), time.min)
            delta = now - midnight
            total_seconds = delta.total_seconds()
            self._last_computed = total_seconds
            self._last_timestamp = time.time()
            return total_seconds

    def get_elapsed_from_midnight_utc(self) -> float:
        with self._lock:
            utcnow = datetime.utcnow()
            midnight_utc = datetime.combine(utcnow.date(), time.min)
            delta = utcnow - midnight_utc
            return delta.total_seconds()

    def get_formatted_elapsed(self) -> str:
        with self._lock:
            elapsed = self._last_computed
            hours = int(elapsed // 3600)
            remainder = elapsed % 3600
            minutes = int(remainder // 60)
            seconds = int(remainder % 60)
            milliseconds = int((elapsed % 1) * 1000)
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"

if __name__ == '__main__':
    calculator = TimeCalculator()
    elapsed = calculator.get_elapsed_from_midnight()
    print(elapsed)
    elapsed_utc = calculator.get_elapsed_from_midnight_utc()
    print(elapsed_utc)
    formatted = calculator.get_formatted_elapsed()
    print(formatted)