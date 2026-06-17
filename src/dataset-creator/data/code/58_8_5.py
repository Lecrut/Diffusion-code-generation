import threading
from datetime import date
from typing import List, Tuple
class DateSpanCalculator:
    def __init__(self):
        self._lock = threading.Lock()
    def calculate_span(self, start_dates: List[date], end_dates: List[date]) -> int:
        if not (len(start_dates) == len(end_dates)):
            raise ValueError("Start and end date lists must have the same length.")
        total_days = 0
        for i in range(len(start_dates)):
            delta = end_dates[i] - start_dates[i]
            with self._lock:
                total_days += delta.days
        return total_days
if __name__ == '__main__':
    calculator = DateSpanCalculator()
    sample_starts = [date(2023, 1, 1), date(2023, 6, 15)]
    sample_ends = [date(2023, 7, 4), date(2023, 8, 20)]
    result = calculator.calculate_span(sample_starts, sample_ends)
    print(f"Total span in days: {result}")