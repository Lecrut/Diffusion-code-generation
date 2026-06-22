from datetime import date

class DaysRemainingCalculator:
    def days_left(self):
        today = date.today()
        last_day_of_month = date(today.year, today.month + 1, 1) - timedelta(days=1)
        return (last_day_of_month - today).days

if __name__ == '__main__':
    calculator = DaysRemainingCalculator()
    print(calculator.days_left())