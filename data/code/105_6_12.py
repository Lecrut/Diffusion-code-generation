import datetime

class DateCalculator:

    def __init__(self, start_date):
        self.start_date = start_date

    def get_next_multiple_of_7(self):
        today = self.start_date
        while True:
            if today.weekday() == 6:
                return today.strftime('%Y-%m-%d')
            today += datetime.timedelta(days=1)
if __name__ == '__main__':
    start_date_str = '2024-01-01'
    calculator = DateCalculator(start_date_str)
    next_multiple_of_7 = calculator.get_next_multiple_of_7()
    print(next_multiple_of_7)