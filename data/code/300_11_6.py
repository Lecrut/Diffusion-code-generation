from datetime import datetime

class DaysRemainingCalculator:
    def days_left(self):
        today = datetime.now()
        last_day_of_month = datetime(today.year, today.month + 1, 1) - timedelta(days=1)
        return (last_day_of_month - today).days

if __name__ == '__main__':
    calculator = DaysRemainingCalculator()
    print(calculator.days_left())