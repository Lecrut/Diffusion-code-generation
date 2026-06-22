import datetime

class DateValidator:
    WEEKEND_MASK = 0xC0

    @staticmethod
    def _parse_date(date_string):
        return datetime.datetime.strptime(date_string, "%Y-%m-%d")

    @classmethod
    def is_weekday(cls, date_string):
        dt_obj = cls._parse_date(date_string)
        weekday_index = dt_obj.weekday()
        return not (weekday_index & cls.WEEKEND_MASK)

if __name__ == '__main__':
    test_dates = ["2023-10-06", "2023-10-07", "2023-10-08"]
    validator = DateValidator()
    outcomes = [validator.is_weekday(d) for d in test_dates]
    print(outcomes)