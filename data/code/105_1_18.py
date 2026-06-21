from datetime import date, timedelta

class DateCalculator:
    def __init__(self, base_date: date):
        self.base_date = base_date

    def find_next_sunday(self) -> date:
        days_ahead = 6 - self.base_date.weekday()
        if days_ahead == 0:
            return self.base_date + timedelta(days=7)
        return self.base_date + timedelta(days=days_ahead)

    def get_base_date(self) -> date:
        return self.base_date

if __name__ == '__main__':
    calc = DateCalculator(date(2024, 1, 1))
    sunday_date = calc.find_next_sunday()
    print(sunday_date)
    print(calc.get_base_date())