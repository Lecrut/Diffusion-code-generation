import datetime

class DateExtractor:
    DAY_ATTRIBUTE = "day"

    def __init__(self, date_obj):
        if not isinstance(date_obj, datetime.date):
            raise ValueError("Input must be a datetime.date object")
        self.date_obj = date_obj

    def get_day_of_month(self):
        return self.date_obj.day

    @staticmethod
    def create_from_parts(year, month, day):
        return DateExtractor(datetime.date(year, month, day))

if __name__ == '__main__':
    sample_date = DateExtractor.create_from_parts(2025, 1, 1)
    day_value = sample_date.get_day_of_month()
    print(day_value)