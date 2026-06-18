import threading
from datetime import date
from typing import List, Tuple
def calculate_date_span(start_dates: List[date], end_dates: List[date]) -> int:
    if len(start_dates) != len(end_dates):
        raise ValueError("Start and end dates must have the same length.")
    spans = []
    lock = threading.Lock()
    for s, e in zip(start_dates, end_dates):
        with lock:
            span_days = (e - s).days
            spans.append(span_days)
    return sum(spans)
if __name__ == '__main__':
    start_list = [date(2023, 1, 1), date(2023, 6, 15)]
    end_list = [date(2023, 7, 4), date(2023, 8, 20)]
    result = calculate_date_span(start_list, end_list)
    print(result)