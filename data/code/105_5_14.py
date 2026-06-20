from datetime import datetime, timedelta

class DateCalculator:
    def __init__(self, target_date):
        self.target_date = datetime.strptime(target_date, "%Y-%m-%d")

    def get_next_wednesday(self):
        days_ahead = (2 - self.target_date.weekday()) % 7
        next_wednesday = self.target_date + timedelta(days=days_ahead)
        return next_wednesday.strftime("%Y-%m-%d")

if __name__ == '__main__':
    calculator = DateCalculator("2023-10-10")
    print(calculator.get_next_wednesday())