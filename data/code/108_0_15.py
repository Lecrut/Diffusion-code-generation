import datetime

DAY_ATTRIBUTE = "day"

class DateExtractor:
    def __init__(self, date_obj):
        if not isinstance(date_obj, datetime.date):
            raise ValueError("Input must be a datetime.date object")
        self.date_obj = date_obj

    def get_day(self):
        return self.date_obj.day

if __name__ == '__main__':
    fixed_date = datetime.date(2025, 1, 1)
    extractor = DateExtractor(fixed_date)
    day_value = extractor.get_day()
    print(day_value)