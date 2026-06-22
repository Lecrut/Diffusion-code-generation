import datetime

class DateChecker:
    WEEKEND_DAYS = (5, 6)

    @staticmethod
    def is_weekend(date_str):
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        return date_obj.weekday() in DateChecker.WEEKEND_DAYS

if __name__ == '__main__':
    print(f"Is 2023-10-07 a weekend? {DateChecker.is_weekend('2023-10-07')}")