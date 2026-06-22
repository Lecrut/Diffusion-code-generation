import datetime

class DateChecker:
    def is_weekend_optimized(self, date):
        weekday = date.weekday()
        return weekday >= 5

if __name__ == '__main__':
    checker = DateChecker()
    date1 = datetime.date(2023, 10, 1)
    print(checker.is_weekend_optimized(date1))
    date2 = datetime.date(2023, 10, 8)
    print(checker.is_weekend_optimized(date2))
    date3 = datetime.date(2023, 10, 9)
    print(checker.is_weekend_optimized(date3))