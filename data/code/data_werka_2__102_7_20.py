import calendar
from datetime import date

class DateValidator:
    def __init__(self, target_date):
        self.target_date = target_date

    def get_weekday_index(self):
        try:
            return calendar.weekday(
                self.target_date.year,
                self.target_date.month,
                self.target_date.day
            )
        except AttributeError:
            return -1

    def is_weekday(self):
        index = self.get_weekday_index()
        return 0 <= index < 5

if __name__ == '__main__':
    sample_date = date(2023, 10, 23)
    validator = DateValidator(sample_date)
    print(validator.is_weekday())
    print(validator.get_weekday_index())