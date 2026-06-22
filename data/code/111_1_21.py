from datetime import date, timedelta
from typing import NamedTuple

class DateArithmeticResult(NamedTuple):
    original: date
    added: date
    formatted: str

class DateCalculator:
    def __init__(self, initial_date: date):
        self.initial_date = initial_date

    def add_days(self, days: int) -> DateArithmeticResult:
        target = self.initial_date + timedelta(days=days)
        formatted = target.strftime("%Y-%m-%d")
        return DateArithmeticResult(self.initial_date, target, formatted)

if __name__ == '__main__':
    calculator = DateCalculator(date(2024, 7, 4))
    result = calculator.add_days(30)
    print(result.formatted)
    print(result.original.isoformat())
    print(result.added.isoformat())