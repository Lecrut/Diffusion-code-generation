from datetime import date

class DateCalculator:
    def __init__(self, date1: str, date2: str):
        self.start_date = date.fromisoformat(date1)
        self.end_date = date.fromisoformat(date2)

    def days_between(self) -> int:
        delta = self.end_date - self.start_date
        return abs(delta.days)

if __name__ == '__main__':
    try:
        calculator = DateCalculator('2023-01-01', '2024-02-29')
        print(calculator.days_between())
    except ValueError as e:
        print(e)