from datetime import date

class DaysRemainingCalculator:
    def days_left(self):
        today = date.today()
        first_day_of_next_month = date(today.year, today.month + 1, 1)
        if first_day_of_next_month.day == 1:
            first_day_of_next_month -= timedelta(days=1)
        return (first_day_of_next_month - today).days

if __name__ == '__main__':
    calculator = DaysRemainingCalculator()
    print(calculator.days_left())