from datetime import timedelta

class DateUtils:
    @staticmethod
    def days_between_dates(date1, date2):
        return abs((date2 - date1).days)

if __name__ == '__main__':
    from datetime import datetime
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 1, 15)
    print(DateUtils.days_between_dates(date1, date2))