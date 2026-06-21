import calendar
from datetime import date

class DateValidator:
    def __init__(self, target_date):
        self.target_date = target_date

    def is_weekday(self):
        try:
            day_index = calendar.weekday(
                self.target_date.year,
                self.target_date.month,
                self.target_date.day
            )
            return day_index < 5
        except AttributeError:
            return False

    def get_day_name(self):
        try:
            day_index = calendar.weekday(
                self.target_date.year,
                self.target_date.month,
                self.target_date.day
            )
            names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            return names[day_index]
        except AttributeError:
            return "Unknown"

if __name__ == '__main__':
    sample_date = date(2023, 10, 23)
    validator = DateValidator(sample_date)
    print(validator.is_weekday())
    print(validator.get_day_name())