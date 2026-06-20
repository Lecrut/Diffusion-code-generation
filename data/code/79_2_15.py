from datetime import datetime, timedelta

class DateCalculator:
    def get_next_month(self):
        today = datetime.now()
        next_month = today.replace(day=1) + timedelta(days=31)
        return next_month.strftime('%Y-%m-%d')

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.get_next_month())