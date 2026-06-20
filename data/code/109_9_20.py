import datetime

class MonthDaysCalculator:
    def __init__(self):
        self.today = datetime.date.today()
    
    @staticmethod
    def get_month_end(current_date):
        if current_date.month == 12:
            return datetime.date(current_date.year + 1, 1, 1) - datetime.timedelta(days=1)
        else:
            return datetime.date(current_date.year, current_date.month + 1, 1) - datetime.timedelta(days=1)

    def calculate_remaining_days(self):
        month_end = self.get_month_end(self.today)
        remaining_days = (month_end - self.today).days
        return remaining_days

if __name__ == '__main__':
    calculator = MonthDaysCalculator()
    time_left = calculator.calculate_remaining_days()
    print(time_left)