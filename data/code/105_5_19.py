from datetime import datetime, timedelta

class DateCalculator:

    def __init__(self, start_date):
        self.start_date = start_date

    def get_next_wednesday(self):
        target_day = 3
        days_to_add = (target_day - self.start_date.weekday() + 7) % 7
        return self.start_date + timedelta(days=days_to_add)
if __name__ == '__main__':
    sample_date_str = '2023-10-10'
    sample_date = datetime.strptime(sample_date_str, '%Y-%m-%d')
    calculator = DateCalculator(sample_date)
    next_wednesday = calculator.get_next_wednesday()
    print(next_wednesday.strftime('%Y-%m-%d'))