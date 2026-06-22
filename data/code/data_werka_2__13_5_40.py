from datetime import date

class DateDurationCalculator:
    def __init__(self, start_date: str, end_date: str):
        self.start_date = date.fromisoformat(start_date)
        self.end_date = date.fromisoformat(end_date)

    def calculate_days(self) -> int:
        delta = self.end_date - self.start_date
        return abs(delta.days)

if __name__ == '__main__':
    calculator1 = DateDurationCalculator('2023-01-01', '2024-02-29')
    print(calculator1.calculate_days())

    calculator2 = DateDurationCalculator('2020-02-28', '2020-03-01')
    print(calculator2.calculate_days())