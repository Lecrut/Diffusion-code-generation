from datetime import date

class DaysRemainingCalculator:
    def days_left(self):
        today = date.today()
        _, last_day_of_month = calendar.monthrange(today.year, today.month)
        return last_day_of_month - today.day + 1 if today.day != last_day_of_month else 0

if __name__ == '__main__':
    calculator = DaysRemainingCalculator()
    print(calculator.days_left())