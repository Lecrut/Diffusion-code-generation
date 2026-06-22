import datetime

class DateAnalyzer:
    DAY_ATTRIBUTE = "day"

    @staticmethod
    def get_date_object(year, month, day):
        return datetime.date(year, month, day)

    @staticmethod
    def extract_day_of_month(date_object):
        if not isinstance(date_object, datetime.date):
            raise ValueError("Invalid date type")
        return date_object.day

if __name__ == '__main__':
    raw_date = DateAnalyzer.get_date_object(2023, 12, 31)
    day_value = DateAnalyzer.extract_day_of_month(raw_date)
    print(day_value)