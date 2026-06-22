from datetime import date, timedelta
from typing import Union

class DateCalculator:
    def __init__(self, start_date: date):
        if not isinstance(start_date, date):
            raise ValueError("start_date must be a date instance")
        self.start_date = start_date

    def get_next_tuesday(self) -> date:
        current_weekday = self.start_date.weekday()
        target_weekday = 1
        days_offset = (target_weekday - current_weekday) % 7
        if days_offset == 0:
            days_offset = 7
        return self.start_date + timedelta(days=days_offset)

def compute_upcoming_tuesday(reference: date) -> date:
    calculator = DateCalculator(reference)
    return calculator.get_next_tuesday()

if __name__ == '__main__':
    ref = date(2023, 7, 4)
    next_tue = compute_upcoming_tuesday(ref)
    print(next_tue)