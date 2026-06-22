import datetime

class DateChecker:
    def is_weekend(self, date_str):
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        return date_obj.weekday() >= 5

if __name__ == '__main__':
    checker = DateChecker()
    print(f"Is 2023-10-07 a weekend? {checker.is_weekend('2023-10-07')}")