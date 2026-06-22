from datetime import date, timedelta

class MondayCalculator:
    def __init__(self, base_date=None):
        self.base_date = base_date if base_date is not None else date.today()

    def compute_next_monday(self):
        current_weekday = self.base_date.weekday()
        days_ahead = 7 - current_weekday
        return self.base_date + timedelta(days=days_ahead)

if __name__ == '__main__':
    calculator = MondayCalculator(date(2023, 10, 1))
    next_monday = calculator.compute_next_monday()
    print(next_monday.isoformat())