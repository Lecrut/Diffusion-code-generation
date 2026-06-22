import calendar

class MonthEndCalculator:
    def __init__(self):
        self.current_year = datetime.datetime.now().year
        self.current_month = datetime.datetime.now().month

    @staticmethod
    def get_days_in_month(year, month):
        return calendar.monthrange(year, month)[1]

    def days_left_in_current_month(self):
        current_day = datetime.datetime.now().day
        days_in_current_month = self.get_days_in_month(self.current_year, self.current_month)
        days_left = days_in_current_month - current_day
        return days_left

if __name__ == '__main__':
    calculator = MonthEndCalculator()
    result = calculator.days_left_in_current_month()
    print(result)