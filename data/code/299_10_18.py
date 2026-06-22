from datetime import date

class WeekendChecker:
    WEEKEND_DAYS = {5, 6}

    @staticmethod
    def is_weekend(year, month, day):
        target_date = date(year, month, day)
        return target_date.weekday() in WeekendChecker.WEEKEND_DAYS
if __name__ == '__main__':
    checker = WeekendChecker()
    print(checker.is_weekend(2023, 10, 7))
    print(checker.is_weekend(2023, 10, 8))
    print(checker.is_weekend(2023, 10, 9))