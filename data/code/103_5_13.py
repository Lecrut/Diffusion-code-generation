import threading
import time
from datetime import datetime, time

class TimeCalculator:
    def __init__(self):
        self._lock = threading.Lock()

    def calculate_elapsed_seconds_from_midnight(self, reference_time: float | None = None) -> float:
        if reference_time is not None:
            if not isinstance(reference_time, (int, float)):
                raise ValueError("reference_time must be a numeric value")
            if reference_time < 0:
                raise ValueError("reference_time must be non-negative")
        
        with self._lock:
            if reference_time is None:
                current_time = time.time()
            else:
                current_time = reference_time
            
            current_datetime = datetime.fromtimestamp(current_time)
            midnight_today = datetime.combine(current_datetime.date(), time.min)
            elapsed = current_datetime - midnight_today
            return elapsed.total_seconds()

def main():
    calculator = TimeCalculator()
    result = calculator.calculate_elapsed_seconds_from_midnight()
    print(result)

if __name__ == '__main__':
    main()