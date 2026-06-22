import calendar
from datetime import date

class DateValidator:
    WEEKDAY_THRESHOLD = 5

    @staticmethod
    def _get_day_index(d):
        return calendar.weekday(d.year, d.month, d.day)

    @classmethod
    def is_weekday(cls, d):
        try:
            day_index = cls._get_day_index(d)
            return day_index < cls.WEEKDAY_THRESHOLD
        except AttributeError:
            return False

if __name__ == '__main__':
    test_date = date(2023, 10, 23)
    result = DateValidator.is_weekday(test_date)
    print(result)