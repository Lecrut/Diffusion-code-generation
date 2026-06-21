from datetime import date, timedelta

class MondayCalculator:
    def __init__(self, current_date=None):
        self.current_date = current_date if current_date is not None else date.today()

    def get_upcoming_monday(self):
        days_ahead = 7 - self.current_date.weekday()
        return self.current_date + timedelta(days=days_ahead)

if __name__ == '__main__':
    calculator = MondayCalculator(date(2023, 10, 2))
    result = calculator.get_upcoming_monday()
    print(result.isoformat())