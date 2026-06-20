import datetime

class DateChecker:
    def is_weekday(self, dt: datetime.datetime) -> bool:
        return dt.weekday() < 5

if __name__ == '__main__':
    checker = DateChecker()
    date1 = datetime.datetime(2023, 10, 25)
    date2 = datetime.datetime(2023, 10, 26)
    print(f"Is {date1} a weekday? {checker.is_weekday(date1)}")
    print(f"Is {date2} a weekday? {checker.is_weekday(date2)}")