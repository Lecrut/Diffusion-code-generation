import calendar
from datetime import date
class DateValidator:
    def __init__(self, d):
        if not isinstance(d, date):
            raise ValueError("Input must be a date object")
        self._date = d
    def is_weekday(self):
        try:
            day_index = calendar.weekday(self._date.year, self._date.month, self._date.day)
            return day_index < 5
        except AttributeError:
            return False
if __name__ == '__main__':
    test_date = date(2024, 1, 15)
    validator = DateValidator(test_date)
    print(validator.is_weekday())