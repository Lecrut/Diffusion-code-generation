from datetime import date, timedelta

class DateCalculator:
    def __init__(self, reference_date: date):
        self.reference_date = reference_date

    def get_next_tuesday(self) -> date:
        days_until_tuesday = (1 + 6 - self.reference_date.weekday()) % 7
        return self.reference_date + timedelta(days=days_until_tuesday)

if __name__ == '__main__':
    calculator = DateCalculator(date(2023, 7, 4))
    upcoming_tuesday = calculator.get_next_tuesday()
    print(upcoming_tuesday)