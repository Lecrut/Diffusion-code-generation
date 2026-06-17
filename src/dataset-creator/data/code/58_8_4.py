import threading
from datetime import date
from typing import List, Tuple
class DateSpanCalculator:
    def __init__(self):
        self._lock = threading.Lock()
    def calculate_span(self, start_dates: List[date], end_dates: List[date]) -> int:
        with self._lock:
            if len(start_dates) != len(end_dates):
                raise ValueError("Start and end date lists must have the same length.")
            total_days = 0
            for s_date in start_dates:
                e_date = end_dates[start_dates.index(s_date)]
                delta = (e_date - s_date).days
                total_days += abs(delta)
            return total_days
def main():
    calc = DateSpanCalculator()
    sample_starts = [date(2023, 1, 1), date(2023, 6, 15)]
    sample_ends = [date(2023, 12, 31), date(2024, 7, 1)]
    result = calc.calculate_span(sample_starts, sample_ends)
    print(f"Total span in days: {result}")
if __name__ == '__main__':
    main()