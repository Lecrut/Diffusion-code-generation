import threading
from datetime import date
from typing import List
class DateSpanCalculator:
    def calculate_span(self, start_dates: List[date], end_dates: List[date]) -> int:
        if len(start_dates) != len(end_dates):
            raise ValueError("Start and end dates lists must have the same length.")
        total_days = 0
        lock = threading.Lock()
        for s_date in range(len(start_dates)):
            delta = end_dates[s_date] - start_dates[s_date]
            with lock:
                total_days += days_in_delta(delta)
        return total_days
def days_in_delta(d: date) -> int:
    if d.days < 0:
        raise ValueError("End date must be after or on the same day as start date.")
    return d.days
if __name__ == '__main__':
    starts = [date(2023, 1, 1), date(2023, 6, 15)]
    ends = [date(2023, 12, 31), date(2024, 7, 4)]
    calculator = DateSpanCalculator()
    result = calculator.calculate_span(starts, ends)
    print(result)