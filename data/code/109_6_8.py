import datetime

class MonthFractionCalculator:

    def __init__(self, current_date):
        self.current_date = current_date

    def calculate_fraction_remaining(self, target_month):
        current_year = self.current_date.year
        current_month = self.current_date.month
        if target_month > current_month:
            target_year = current_year
        else:
            target_year = current_year - 1
        days_in_current_month = (self.current_date.replace(day=28) + datetime.timedelta(days=4)).day
        return (days_in_current_month - self.current_date.day) / days_in_current_month
if __name__ == '__main__':
    calculator = MonthFractionCalculator(datetime.date(2023, 10, 15))
    print(calculator.calculate_fraction_remaining(11))