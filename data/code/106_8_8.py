from datetime import datetime

class YearDifferenceCalculator:
    def __init__(self, reference_date: datetime):
        self.reference_date = reference_date

    def compute(self, target_date: datetime) -> int:
        delta = target_date - self.reference_date
        years = delta.days // 365
        if years < 0 and delta.days % 365 != 0:
            years -= 1
        elif years > 0 and delta.days % 365 != 0:
            years += 1
        return years

if __name__ == '__main__':
    start = datetime(2000, 1, 1)
    end = datetime(2024, 12, 31)
    calculator = YearDifferenceCalculator(start)
    result = calculator.compute(end)
    print(result)
    past_date = datetime(1990, 6, 15)
    past_result = calculator.compute(past_date)
    print(past_result)