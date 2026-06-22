from datetime import datetime, timedelta

class DateCalculator:
    def __init__(self, reference_date):
        self.reference_date = reference_date

    def get_weekday_index(self, date):
        return date.weekday()

    def get_days_until_friday(self):
        current_index = self.get_weekday_index(self.reference_date)
        target_index = 4
        days_ahead = target_index - current_index
        if days_ahead <= 0:
            days_ahead += 7
        return days_ahead

    def get_upcoming_friday(self):
        days = self.get_days_until_friday()
        return self.reference_date + timedelta(days=days)

    def format_date(self, date):
        return date.strftime("%Y-%m-%d")

if __name__ == '__main__':
    ref_date = datetime(2023, 12, 15)
    calculator = DateCalculator(ref_date)
    friday_date = calculator.get_upcoming_friday()
    formatted_friday = calculator.format_date(friday_date)
    days_calc = calculator.get_days_until_friday()
    print(formatted_friday)
    print(days_calc)