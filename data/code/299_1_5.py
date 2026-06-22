import datetime

class DateChecker:
    def __init__(self, date_str):
        self.date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

    def is_weekend(self):
        return self.date_obj.weekday() >= 5

if __name__ == '__main__':
    checker = DateChecker('2023-10-07')
    print(f"Is the date {checker.date_obj} a weekend? {checker.is_weekend()}")