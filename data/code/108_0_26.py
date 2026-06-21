import datetime

class DateExtractor:
    DAY_OF_MONTH = "day_of_month"

    @staticmethod
    def extract_day(date_obj):
        if not isinstance(date_obj, datetime.date):
            raise ValueError("date_obj must be a datetime.date instance")
        return date_obj.day

if __name__ == '__main__':
    target_date = datetime.date(2025, 3, 14)
    extractor = DateExtractor()
    day_value = extractor.extract_day(target_date)
    print(day_value)