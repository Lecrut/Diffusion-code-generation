from datetime import date

class DateDifferenceCalculator:
    def __init__(self, start_date: str, end_date: str):
        self.start_date = self._parse_date(start_date)
        self.end_date = self._parse_date(end_date)

    @staticmethod
    def _parse_date(date_str: str) -> date:
        parts = date_str.split('-')
        return date(int(parts[0]), int(parts[1]), int(parts[2]))

    def total_days(self) -> int:
        delta = self.end_date - self.start_date
        return delta.days

    def absolute_days(self) -> int:
        return abs(self.total_days())

    def in_weeks(self) -> int:
        return abs(self.total_days()) // 7

if __name__ == '__main__':
    calc = DateDifferenceCalculator('2023-01-01', '2023-12-31')
    print(calc.total_days())
    print(calc.absolute_days())
    print(calc.in_weeks())