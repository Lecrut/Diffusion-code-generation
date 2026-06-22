import calendar

class MonthDaysCalculator:
    def __init__(self):
        self.current_date = datetime.date.today()

    @staticmethod
    def days_in_month(year, month):
        return calendar.monthrange(year, month)[1]

    def calculate_remaining_days(self, target_month, target_year):
        days_in_target_month = self.days_in_month(target_year, target_month)
        first_day_of_target_month = datetime.date(target_year, target_month, 1)
        if self.current_date < first_day_of_target_month:
            remaining_days = days_in_target_month - (self.current_date.day - 1)
        else:
            remaining_days = days_in_target_month - (self.current_date.day)
        return remaining_days

if __name__ == '__main__':
    calculator = MonthDaysCalculator()
    target_month = 12
    target_year = 2024
    result = calculator.calculate_remaining_days(target_month, target_year)
    print(result)