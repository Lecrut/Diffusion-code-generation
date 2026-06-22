from datetime import datetime

class YearSpanCalculator:
    def __init__(self, reference_date: datetime):
        self.reference_date = reference_date

    def calculate(self, target_date: datetime) -> int:
        years = target_date.year - self.reference_date.year
        if target_date.month < self.reference_date.month:
            years -= 1
        elif target_date.month == self.reference_date.month:
            if target_date.day < self.reference_date.day:
                years -= 1
        return abs(years)

if __name__ == '__main__':
    start = datetime(2018, 3, 15)
    end = datetime(2023, 3, 14)
    calculator = YearSpanCalculator(start)
    print(calculator.calculate(end))
    print(calculator.calculate(datetime(2023, 3, 15)))