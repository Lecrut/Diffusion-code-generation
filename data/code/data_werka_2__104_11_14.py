from datetime import datetime

class DayDifferenceCalculator:
    def __init__(self, start: datetime, end: datetime):
        if start.tzinfo is not None or end.tzinfo is not None:
            raise ValueError("Timezone-aware datetimes are not supported for naive comparison.")
        self.start = start
        self.end = end

    def calculate(self) -> int:
        delta = self.end - self.start
        return delta.days

if __name__ == '__main__':
    start_date = datetime(2023, 5, 1, 0, 0, 0)
    end_date = datetime(2023, 5, 15, 23, 59, 59)
    calculator = DayDifferenceCalculator(start_date, end_date)
    days_diff = calculator.calculate()
    print(days_diff)
    extended_end = datetime(2023, 6, 1, 0, 0, 0)
    calculator.start = start_date
    calculator.end = extended_end
    print(calculator.calculate())