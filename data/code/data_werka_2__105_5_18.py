from datetime import date, timedelta

class DateCalculator:
    WEDNESDAY_INDEX = 2
    WEEK_LENGTH = 7

    def __init__(self, reference_date: date):
        self.reference_date = reference_date

    def get_next_wednesday(self) -> date:
        current_weekday = self.reference_date.weekday()
        days_until_wednesday = self.WEDNESDAY_INDEX - current_weekday
        if days_until_wednesday <= 0:
            days_until_wednesday += self.WEEK_LENGTH
        return self.reference_date + timedelta(days=days_until_wednesday)

    def get_days_difference(self, target_date: date) -> int:
        return (target_date - self.reference_date).days

if __name__ == '__main__':
    calc = DateCalculator(date(2023, 10, 10))
    next_wed = calc.get_next_wednesday()
    print(next_wed)
    print(calc.get_days_difference(next_wed))