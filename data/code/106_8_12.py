from datetime import datetime

class YearDifferenceCalculator:
    def __init__(self, reference_date: datetime):
        self.reference_date = reference_date

    def calculate(self, target_date: datetime) -> int:
        delta = target_date - self.reference_date
        years = delta.days // 365
        if (delta.days < 0) != (years < 0):
            years += 1
        return abs(years)

if __name__ == '__main__':
    ref = datetime(2020, 6, 15)
    calc = YearDifferenceCalculator(ref)
    d1 = datetime(2025, 6, 14)
    d2 = datetime(2015, 6, 16)
    print(calc.calculate(d1))
    print(calc.calculate(d2))