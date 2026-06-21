from datetime import datetime

class YearDifferenceCalculator:
    def __init__(self, reference_date: datetime):
        self.reference_date = reference_date

    def calculate(self, target_date: datetime) -> int:
        delta = target_date - self.reference_date
        days = delta.days
        years = abs(days) // 365
        if days < 0:
            return -years
        return years

if __name__ == '__main__':
    ref = datetime(2020, 1, 1)
    calc = YearDifferenceCalculator(ref)
    target1 = datetime(2023, 1, 1)
    target2 = datetime(2018, 12, 31)
    print(calc.calculate(target1))
    print(calc.calculate(target2))