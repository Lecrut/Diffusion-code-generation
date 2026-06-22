from datetime import date, timedelta

WEDNESDAY_INDEX = 2
WEEK_LENGTH = 7

class DateCalculator:
    def __init__(self, reference_date: date):
        self.reference_date = reference_date

    def get_next_weekday(self, target_weekday: int) -> date:
        current_weekday = self.reference_date.weekday()
        days_until_target = target_weekday - current_weekday
        if days_until_target <= 0:
            days_until_target += WEEK_LENGTH
        return self.reference_date + timedelta(days=days_until_target)

    def get_reference_date(self) -> date:
        return self.reference_date

if __name__ == '__main__':
    start_date = date(2023, 10, 10)
    calculator = DateCalculator(start_date)
    next_wed = calculator.get_next_weekday(WEDNESDAY_INDEX)
    ref = calculator.get_reference_date()
    print(ref)
    print(next_wed)