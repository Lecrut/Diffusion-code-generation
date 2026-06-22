from datetime import date

class DateChecker:
    def is_weekend(self, year, month, day):
        return date(year, month, day).weekday() >= 5

if __name__ == '__main__':
    checker = DateChecker()
    print(checker.is_weekend(2023, 10, 7))
    print(checker.is_weekend(2023, 10, 8))