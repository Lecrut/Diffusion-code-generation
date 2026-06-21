import calendar
from datetime import date

class DateValidator:
    WEEKDAY_THRESHOLD = 5

    @staticmethod
    def is_weekday_check(target_date):
        if not isinstance(target_date, date):
            raise ValueError("Input must be a date instance")
        try:
            day_code = calendar.weekday(target_date.year, target_date.month, target_date.day)
            return day_code < DateValidator.WEEKDAY_THRESHOLD
        except AttributeError:
            return False

if __name__ == '__main__':
    test_date = date(2023, 10, 23)
    validator = DateValidator()
    result = validator.is_weekday_check(test_date)
    print(result)