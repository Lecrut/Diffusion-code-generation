import datetime

class DateCalculator:
    def __init__(self):
        self.today = datetime.date.today()

    @staticmethod
    def days_in_month(year, month):
        _, last_day = calendar.monthrange(year, month)
        return last_day

    def remaining_days(self, year, month):
        if self.today.year == year and self.today.month < month:
            first_day_of_next_month = datetime.date(year, month, 1)
            return (first_day_of_next_month - self.today).days
        elif self.today.year < year:
            first_day_of_next_year = datetime.date(year, 1, 1)
            return (first_day_of_next_year - self.today).days
        else:
            days_in_current_month = DateCalculator.days_in_month(self.today.year, self.today.month)
            return days_in_current_month - self.today.day

if __name__ == '__main__':
    calculator = DateCalculator()
    remaining = calculator.remaining_days(2024, 12)
    print(remaining)