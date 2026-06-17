import threading
from datetime import date
from typing import List, Tuple
class DateSpanCalculator:
    def __init__(self):
        self._lock = threading.Lock()
    def calculate_span(self, start_dates: List[date], end_dates: List[date]) -> int:
        if len(start_dates) != len(end_dates):
            raise ValueError("Start and end date lists must have the same length.")
        total_days = 0
        with self._lock:
            for s_date in start_dates:
                e_date = end_dates[start_dates.index(s_date)]
                delta = (e_date - s_date).days
                total_days += abs(delta)
        return total_days
if __name__ == '__main__':
    calc = DateSpanCalculator()
    sample_starts = [date(2023, 1, 1), date(2023, 6, 15)]
    sample_ends = [date(2023, 12, 31), date(2024, 7, 4)]
    result = calc.calculate_span(sample_starts, sample_ends)
    print(result)