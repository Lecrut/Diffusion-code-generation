from datetime import date

class MonthCalculator:
    def days_left_in_month(self):
        today = date.today()
        year, month = today.year, today.month
        _, last_day_of_month = date(year, month + 1, 1).isocalendar()[:2]
        return last_day_of_month - today.day

if __name__ == '__main__':
    calculator = MonthCalculator()
    days_left = calculator.days_left_in_month()
    print(days_left)