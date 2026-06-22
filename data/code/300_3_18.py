from datetime import date, timedelta

class MonthDaysCalculator:
    def days_left_in_month(self):
        today = date.today()
        last_day_of_month = date(today.year, today.month + 1, 1) - timedelta(days=1)
        return (last_day_of_month - today).days

if __name__ == '__main__':
    calculator = MonthDaysCalculator()
    days_left = calculator.days_left_in_month()
    print(days_left)