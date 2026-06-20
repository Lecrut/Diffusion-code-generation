from datetime import datetime, timedelta

class DateCalculator:
    def get_next_month(self):
        current_date = datetime.now()
        next_month = current_date.replace(day=28) + timedelta(days=4)
        return next_month.replace(day=1)

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.get_next_month())