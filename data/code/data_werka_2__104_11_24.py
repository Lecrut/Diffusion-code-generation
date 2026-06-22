from datetime import datetime

class DateDeltaCalculator:
    def __init__(self, reference: datetime):
        self.reference = reference

    def get_days_to(self, target: datetime) -> int:
        if self.reference.tzinfo is not None:
            raise ValueError("Reference datetime must be naive.")
        if target.tzinfo is not None:
            raise ValueError("Target datetime must be naive.")
        delta = target - self.reference
        return delta.days

    def get_days_from(self, source: datetime) -> int:
        if source.tzinfo is not None:
            raise ValueError("Source datetime must be naive.")
        if self.reference.tzinfo is not None:
            raise ValueError("Reference datetime must be naive.")
        delta = self.reference - source
        return delta.days

if __name__ == '__main__':
    base_date = datetime(2023, 6, 15, 9, 0, 0)
    calculator = DateDeltaCalculator(base_date)
    
    future_date = datetime(2023, 6, 20, 14, 30, 0)
    past_date = datetime(2023, 6, 10, 8, 0, 0)
    
    print(calculator.get_days_to(future_date))
    print(calculator.get_days_from(past_date))