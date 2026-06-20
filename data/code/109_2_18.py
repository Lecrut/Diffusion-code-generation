import datetime

class DateCalculator:
    def __init__(self):
        self.today = datetime.date.today()

    @staticmethod
    def get_first_day_of_next_month(year, month):
        if month == 12:
            return datetime.date(year + 1, 1, 1)
        else:
            return datetime.date(year, month + 1, 1)

    def calculate_time_remaining(self, year, month, day):
        next_month_start = self.get_first_day_of_next_month(year, month)
        time_remaining = (next_month_start - self.today).days
        return datetime.timedelta(days=time_remaining)

if __name__ == '__main__':
    calculator = DateCalculator()
    sample_year = 2023
    sample_month = 10
    sample_day = 15
    time_left = calculator.calculate_time_remaining(sample_year, sample_month, sample_day)
    print(time_left)