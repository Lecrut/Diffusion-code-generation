import datetime

class DateChecker:
    def __init__(self, year, month, day):
        self.date = datetime.date(year, month, day)

    def is_weekday(self):
        return self.date.weekday() < 5

if __name__ == '__main__':
    checker = DateChecker(2023, 10, 25)
    print(checker.is_weekday())