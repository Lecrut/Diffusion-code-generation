from datetime import date
import calendar

class DateCalculator:
    def __init__(self, start_date: date):
        self.start_date = start_date

    def get_next_15th(self) -> date:
        year = self.start_date.year
        month = self.start_date.month
        day = self.start_date.day

        if day <= 15:
            target_month = month
            target_year = year
        else:
            target_month = month + 1
            target_year = year

        if target_month > 12:
            target_month = 1
            target_year += 1

        return date(target_year, target_month, 15)

    def get_days_until_15th(self) -> int:
        next_15th = self.get_next_15th()
        delta = next_15th - self.start_date
        return delta.days

if __name__ == '__main__':
    calculator = DateCalculator(date(2023, 3, 3))
    next_15th = calculator.get_next_15th()
    days_until = calculator.get_days_until_15th()
    print(next_15th)
    print(days_until)