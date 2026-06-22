import datetime

class DateUtils:
    def __init__(self, target_year, target_month):
        self.target_date = datetime.date(target_year, target_month, 1)
        self.year_end = datetime.date(target_year, 12, 31)

    def calculate_remaining_days(self):
        remaining_days = (self.year_end - self.target_date).days + 1
        return remaining_days

if __name__ == '__main__':
    target_month = 2
    target_year = 2024
    date_utils = DateUtils(target_year, target_month)
    result = date_utils.calculate_remaining_days()
    print(result)