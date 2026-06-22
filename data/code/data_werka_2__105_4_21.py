from datetime import date, timedelta

class CalendarCalculator:
    SATURDAY_INDEX = 5

    def __init__(self, base_date: date):
        self.base_date = base_date

    def days_to_next_saturday(self) -> int:
        current_weekday = self.base_date.weekday()
        delta = self.SATURDAY_INDEX - current_weekday
        if delta <= 0:
            delta += 7
        return delta

    def compute_target_date(self) -> date:
        return self.base_date + timedelta(days=self.days_to_next_saturday())

if __name__ == '__main__':
    fixed_start = date(2023, 11, 1)
    calculator = CalendarCalculator(fixed_start)
    target = calculator.compute_target_date()
    print(target)