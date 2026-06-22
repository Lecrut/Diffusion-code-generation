from datetime import date
from typing import Tuple

def compute_year_span(d1: date, d2: date) -> int:
    if not isinstance(d1, date) or not isinstance(d2, date):
        raise ValueError("Inputs must be date instances")
    if d1 > d2:
        d1, d2 = d2, d1
    years = d2.year - d1.year
    if d2.month < d1.month:
        years -= 1
    elif d2.month == d1.month and d2.day < d1.day:
        years -= 1
    return years

class DateAnalyzer:
    def __init__(self, start: date, end: date):
        self.start = start
        self.end = end

    def get_span(self) -> int:
        return compute_year_span(self.start, self.end)

if __name__ == '__main__':
    d1 = date(2010, 6, 15)
    d2 = date(2023, 5, 10)
    analyzer = DateAnalyzer(d1, d2)
    span = analyzer.get_span()
    print(span)