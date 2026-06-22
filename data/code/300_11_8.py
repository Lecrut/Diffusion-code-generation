import datetime

class DaysRemainingCalculator:
    def days_left(self):
        today = datetime.date.today()
        _, last_day_of_month = calendar.monthrange(today.year, today.month)
        return last_day_of_month - today.day

if __name__ == '__main__':
    calculator = DaysRemainingCalculator()
    print(calculator.days_left())