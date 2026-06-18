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
        for i in range(len(start_dates)):
            with self._lock:
                start_day = start_dates[i].toordinal()
                end_day = end_dates[i].toordinal()
                span = abs(end_day - start_day)
                total_days += span
        return total_days
if __name__ == '__main__':
    calc = DateSpanCalculator()
    starts = [date(2023, 1, 1), date(2023, 6, 15)]
    ends = [date(2023, 12, 31), date(2024, 7, 4)]
    result = calc.calculate_span(starts, ends)
    print(result)