import datetime

class WeekdayChecker:
    def __init__(self):
        self.sample_dt = datetime.datetime(2023, 10, 10)

    def is_weekday(self, dt):
        return dt.weekday() < 5

if __name__ == '__main__':
    checker = WeekdayChecker()
    print(checker.is_weekday(checker.sample_dt))
    print(checker.is_weekday(datetime.datetime(2023, 10, 24)))
    print(checker.is_weekday(datetime.datetime(2023, 10, 26)))