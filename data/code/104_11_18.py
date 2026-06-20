import datetime

class DateDifferenceCalculator:

    @staticmethod
    def calculate_days_difference(date1, date2):
        if not isinstance(date1, datetime.datetime) or not isinstance(date2, datetime.datetime):
            raise ValueError('Both inputs must be instances of datetime.datetime')
        if date1.tzinfo is None:
            date1 = date1.replace(tzinfo=datetime.timezone.utc)
        if date2.tzinfo is None:
            date2 = date2.replace(tzinfo=datetime.timezone.utc)
        delta = date2 - date1
        return abs(delta.days)
if __name__ == '__main__':
    d1 = datetime.datetime(2023, 10, 26, 10, 30, 0, tzinfo=datetime.timezone.utc)
    d2 = datetime.datetime(2023, 10, 25, 15, 45, 0, tzinfo=datetime.timezone.utc)
    print(DateDifferenceCalculator.calculate_days_difference(d1, d2))