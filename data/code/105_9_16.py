from datetime import date, timedelta

class DateCalculator:
    def __init__(self, start_date):
        self.start_date = start_date

    def get_next_monday(self):
        days_ahead = (0 - self.start_date.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return self.start_date + timedelta(days=days_ahead)

    def get_next_monday_str(self):
        next_monday = self.get_next_monday()
        return next_monday.strftime('%Y-%m-%d')

if __name__ == '__main__':
    calculator = DateCalculator(date(2024, 2, 28))
    print(calculator.get_next_monday())
    print(calculator.get_next_monday_str())