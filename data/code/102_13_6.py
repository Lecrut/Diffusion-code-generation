import datetime

class DateChecker:
    WEEKDAY_RANGE = (0, 4)

    @staticmethod
    def is_weekday(dt: datetime.datetime) -> bool:
        return DateChecker.WEEKDAY_RANGE[0] <= dt.weekday() <= DateChecker.WEEKDAY_RANGE[1]

if __name__ == '__main__':
    date1 = datetime.datetime(2023, 10, 25)
    date2 = datetime.datetime(2023, 10, 26)
    date3 = datetime.datetime(2023, 10, 27)
    date4 = datetime.datetime(2023, 10, 28)
    print(f"Is {date1} a weekday? {DateChecker.is_weekday(date1)}")
    print(f"Is {date2} a weekday? {DateChecker.is_weekday(date2)}")
    print(f"Is {date3} a weekday? {DateChecker.is_weekday(date3)}")
    print(f"Is {date4} a weekday? {DateChecker.is_weekday(date4)}")