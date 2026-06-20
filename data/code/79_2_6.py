from datetime import date, timedelta

class DateCalculator:
    def get_next_month(self):
        today = date.today()
        next_month = today.replace(day=28) + timedelta(days=4)
        return next_month.replace(day=1)

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.get_next_month())