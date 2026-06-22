import datetime

class DaysRemainingCalculator:
    def days_left(self):
        today = datetime.date.today()
        last_day_of_month = datetime.date(today.year, today.month, 1) + datetime.timedelta(days=32)
        return (last_day_of_month - today).days

if __name__ == '__main__':
    calculator = DaysRemainingCalculator()
    print(calculator.days_left())