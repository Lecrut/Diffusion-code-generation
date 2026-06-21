import threading
from datetime import datetime, time, timedelta

class TimeCalculator:
    def __init__(self, reference: datetime | None = None):
        if reference is None:
            reference = datetime.now()
        self.reference = reference
        self._lock = threading.Lock()

    def get_elapsed_seconds_from_midnight(self) -> float:
        with self._lock:
            today = self.reference.date()
            midnight = datetime.combine(today, time.min)
            delta = self.reference - midnight
            return delta.total_seconds()

def calculate_elapsed_seconds() -> float:
    calculator = TimeCalculator()
    return calculator.get_elapsed_seconds_from_midnight()

if __name__ == '__main__':
    value = calculate_elapsed_seconds()
    print(value)