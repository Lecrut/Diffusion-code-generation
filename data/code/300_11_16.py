import datetime

class DaysRemainingCalculator:
    def days_left(self):
        today = datetime.date.today()
        first_day_of_next_month = datetime.date(today.year, today.month + 1, 1)
        if first_day_of_next_month.month == 1:
            first_day_of_next_month = datetime.date(today.year + 1, 1, 1)
        return (first_day_of_next_month - today).days

if __name__ == '__main__':
    calculator = DaysRemainingCalculator()
    print(calculator.days_left())